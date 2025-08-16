# certbot简易手册（Nginx）

## 一、安装

### 1. 更新系统

```bash
sudo apt update
sudo apt upgrade -y
```

### 2. 安装 Certbot 与 Nginx 插件

```bash
sudo apt install certbot python3-certbot-nginx -y
```


## 二、申请证书

### 方式一：HTTP-01 验证（自动配置，需公网可访问）

适用场景：公网可访问 80/443 端口的服务器

```bash
sudo certbot --nginx
```

执行后：

* Certbot 会检测 Nginx 配置中的域名
* 自动与 Let’s Encrypt 交互，申请证书
* 自动修改 Nginx 配置并启用 HTTPS

#### 多域名示例

```bash
sudo certbot --nginx -d example.com -d www.example.com
```


### 方式二：DNS-01 验证（手动模式，可用于内网或通配符）

适用场景：

* 服务器无法公网访问
* 需要申请通配符证书（`*.example.com`）

```bash
sudo certbot certonly --manual --preferred-challenges dns -d example.com -d '*.example.com'
```

执行后，Certbot 会提示你添加 DNS TXT 记录，例如：

```
_acme-challenge.example.com   TXT   abcd1234efgh5678ijkl
```

#### 检查 DNS 是否生效

```bash
dig -t txt _acme-challenge.example.com
```

确认 TXT 记录正确解析后，回到 Certbot 界面按 **Enter** 继续，生成证书。


## 三、常用命令

* **查看证书**

  ```bash
  sudo certbot certificates
  ```

* **手动续期**

  ```bash
  sudo certbot renew
  ```

* **测试续期**

  ```bash
  sudo certbot renew --dry-run
  ```

* **仅申请证书，不改 Nginx 配置**

  ```bash
  sudo certbot certonly --nginx
  ```


## 四、证书路径

证书默认存放在：

```
/etc/letsencrypt/live/你的域名/
```

常用文件：

* `fullchain.pem` —— 公钥证书
* `privkey.pem` —— 私钥


## 五、Nginx 配置示例

Certbot 自动配置后，Nginx 配置类似：

```nginx
server {
    listen 80;
    server_name example.com www.example.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name example.com www.example.com;

    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

    location / {
        root /var/www/html;
        index index.html;
    }
}
```


## 六、自动续期

Certbot 安装时会自动添加定时任务或 systemd timer 来续期证书。
手动检查：

```bash
systemctl list-timers | grep certbot
```


## 七、常见问题

1. **80/443 端口不可访问，申请失败**

   * 检查防火墙/安全组规则
   * 确认 Nginx 监听 80 端口

2. **申请通配符证书**

   * 只能用 DNS-01 验证
   * 示例：

     ```bash
     sudo certbot certonly --manual --preferred-challenges dns -d '*.example.com'
     ```

3. **内网环境申请**

   * 使用 DNS-01 验证
   * 不依赖公网访问，只需能修改 DNS


📌 **总结：**

* **公网可访问** → `sudo certbot --nginx`（自动配置）
* **内网 / 通配符** → `sudo certbot certonly --manual --preferred-challenges dns`（手动模式）
* **续期** → `sudo certbot renew`
