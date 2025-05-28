# 从本地上传文件

!!! warning
    下面的命令是对于使用dockers运行的nextcloud的，如果是直接安装在本地，请注意。

## 步骤

### 1.复制文件

这就不用多说了，一般路径为`/nextcloud/data/<username>/files`。  

### 2.更新权限

对于上传的文件，需要更新其权限，不然没有办法修改和删除，nextcloud使用的用户是`www-data`。  

```bash
chown -R www-data:www-data <TARGET_DIR>
```

只更新上传到的目录就行，或者指定文件。  

### 3.扫描

使用OCC命令更新文件索引。  

occ有三个用于管理Nextcloud中文件的命令：
```
files
 files:cleanup              #清除文件缓存
 files:scan                 #重新扫描文件系统
 files:transfer-ownership   #将所有文件和文件夹都移动到另一个文件夹
```

对于docker的container，使用如下命令扫描  
```bash
docker exec -u www-data <container name> php /var/www/html/occ files:scan --path <user name>/files/<path>/
```

!!! warning
    注意，`--path`后的路径参数是基于`data`文件夹下的相对路径，所以只需要从用户名开始写就行

或者扫描整个目录  
```bash
docker exec -u www-data <container name> php /var/www/html/occ files:scan --all
```

## Reference

1. [手动拷贝文件至nextcloud中并扫描（docker）-博客园](https://www.cnblogs.com/xiangfeigao/p/17348311.html)
2. [Nextcloud如何手动增加文件；手动恢复nextcloud已有数据；nextcloud备份文件的恢复-知乎](https://zhuanlan.zhihu.com/p/458671872)