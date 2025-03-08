# Nginx将http反向代理到https

## 1.安装nginx

## 2.在/etc/nginx/conf.d下建立nginx反向代理文件

例如 website.conf:  
```conf
server {
    server_name xxx.xxx.xxx;  # 要分发证书的域名

    location / {
        proxy_pass https://localhost:port;  # 将port反向代理到HTTPS，如果你的原网址是http，要改过来
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

退出编辑，测试nginx  
```shell
nginx -t
```

重启nginx  
```shell
systemctl reload nginx
```

## 安装certbot和nginx插件

安装certbot和插件  

```shell
apt install certbot python3-certbot-nginx
```

使用certbot自动检测nginx配置并分发证书  
```shell
certbot --nginx
```

## 检查certbot定时刷新证书服务状态

```shell
systemctl status certbot.timer
```

手动测试证书续期是否工作：  
```shell
certbot renew --dry-run
```