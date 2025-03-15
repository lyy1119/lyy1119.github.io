# 使用docker快速搭建nextcloud

参考：[Docker安装Nextcloud，非AIO方式，并配置HTTPS](https://www.bilibili.com/opus/828057484080971780)  

建议先阅读完再操作  

## 1.docker-compose.yml

请仔细阅读下面的yml文件。按需求更改后启动。  

```yml
networks:
  default:
    name: nextcloud

services:
  app:
    image: nextcloud:latest
    restart: unless-stopped
    volumes:
      - /SATA/Nextcloud/config:/var/www/html/config  # 这是文件数据存储位置，注意更改，前面的是宿主机位置
      - /SATA/Nextcloud/data:/var/www/html/data
    environment:
      - MYSQL_PASSWORD=nextcloud_password # 按需修改，可不更改，和下面db服务的对应就行
      - MYSQL_DATABASE=nextcloud
      - MYSQL_USER=nextcloud
      - MYSQL_HOST=db
      - TZ=Asia/Shanghai
      - PHP_UPLOAD_LIMIT=50G
      - PHP_MEMORY_LIMIT=8G
    ports:
      - 51111:80 # 按需修改 ，前者为宿主机端口
    networks:
      - default

  cache:
    image: redis:latest
    restart: unless-stopped
    expose:
     - "6379" # 可用此默认。因为这是暴露而不是映射
    volumes:
     - /SATA/Nextcloud/docker_cache:/data # 需要修改
    command: redis-server --requirepass 'redis_password' # 按需修改
    environment:
      - TZ=Asia/Shanghai
    networks:
      - default

  db:
    image: mariadb:latest
    restart: unless-stopped
    # 下面的command与官网略有不同。它将有助于避免MYSQL数据库的4047报错。
    command: --transaction-isolation=READ-COMMITTED --binlog-format=ROW --innodb-file-per-table=1 --skip-innodb-read-only-compressed
    volumes:
      - /SATA/Nextcloud/docker_db:/var/lib/mysql
    environment:
      - MYSQL_ROOT_PASSWORD=nextcloud_mysql_password # 按需修改，可不更改
      - MYSQL_PASSWORD=nextcloud_password  # 按需修改，可不更改
      - MYSQL_DATABASE=nextcloud
      - MYSQL_USER=nextcloud
      - TZ=Asia/Shanghai
    networks:
      - default
```

## 2.启动

```bash
docker-compose up -d
```

启动后进入页面设置管理员账号和密码。端口为上一步设置的`app`下的ports。  


## 3.配置网盘的缓存

去上一步中设置的config位置，找到其中的`config.php`。做以下修改：  

![20250315120338](https://raw.githubusercontent.com/lyy1119/Imgs/main/img/20250315120338.png)  

即在第三行下添加如下内容：  
```php
  'memcache.distributed' => '\\OC\\Memcache\\Redis',
  'memcache.locking' => '\\OC\\Memcache\\Redis',
  'redis' => array(
          'host' => 'cache',
          'port' => 6379,
          'password' => 'redis_password'
  ),
```

在任意位置添加下面这行以支持中国电话号码（注意前后行逗号问题）：  
```php
'default_phone_region' => 'CN',
```

修改配置后保存即可，无需重启。  


## 4.修改后台任务的配置

进入网页端：**管理设置** -> **基本设置** -> **后台任务**  

将选项改为`cron`。  

![20250315123011](https://raw.githubusercontent.com/lyy1119/Imgs/main/img/20250315123011.png)  

现在需要在服务器上设置cron任务，具体来说，通过宿主机执行`docker exec ...`来实现cron。  

先使用`docker ps`确定docker容器的名称，如果你没有更改docker-compose中的相应部分的话，那么应该是`nextcloud_app_1`。  

运行以下命令来测试（也就是宿主机执行cron的命令）：  
```bash
docker exec -u www-data nextcloud_app_1 php cron.php
```

如果没有写错的话，可以在 **管理设置** -> **基本设置** -> **后台任务** 中看到 “ **上次任务执行于 a few seconds ago。** ”  

在命令行下输入:  
```bash
crontab -e
```

编写cron：  
```cron
*/5 * * * * docker exec -u www-data nextcloud_app_1 php cron.php
```  

这条语句的含义是每5分钟执行刚刚的cron命令。  

## 5.解决上传大文件出错问题

[原文](https://blog.csdn.net/linyy031119/article/details/142242468?spm=1001.2014.3001.5501)  

先进入docker容器，修改apache2的配置。  

```bash
docker exec -it nextcloud_app_1 /bin/bash
```

自行安装文本编辑器（不知道的可以搜索： **debian如何安装vim** ）  

修改文件 `/etc/apache2/sites-available/000-default.conf`  

添加 LimitRequestBody 0，如下:  

```yml
<VirtualHost *:80>
    ...
    LimitRequestBody 0
    ...
</VirtualHost>
```

保存退出即可。  

## 6.nginx反向代理到https

见我的另一篇文章 **Nginx将http反向代理到https** 。  

可能出现client_max_body_size太小导致上传的问题，在nginx里设置即可。  
在http模块下写，如：`client_max_body_size 125m;`  