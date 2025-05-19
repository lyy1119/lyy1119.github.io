# 反向代理实现Github加速

有时候服务器不好连接github，这样clone代码就很麻烦，可以在能访问GitHub的服务器上搭建Nginx反向代理来解决这一问题。  

目前的nginx配置文件仅尝试过下载raw和clone代码：  

## raw.githubusercontent

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location /github/raw/ {
        proxy_pass https://raw.githubusercontent.com/;
        proxy_redirect off;

        # 保留原始 Host 和请求头
        proxy_set_header Host raw.githubusercontent.com;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # 设置 CORS 跨域头
        add_header Access-Control-Allow-Origin *;
        add_header Access-Control-Allow-Methods 'GET, POST, OPTIONS';
        add_header Access-Control-Allow-Headers '*';

        # 对预检请求立即返回 204
        if ($request_method = OPTIONS ) {
            add_header Content-Length 0;
            add_header Content-Type text/plain;
            return 204;
        }
    }

}
```

## github.com

记得使用certbot做成https。  

```nginx
server {
    listen 80;
    server_name github.yourdomain.com;  # 你自定义的域名

    location / {
        proxy_pass https://github.com/;
        proxy_redirect off;

        proxy_set_header Host github.com;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # 跨域处理，仅供浏览器访问用（clone 用不上）
        add_header Access-Control-Allow-Origin *;
        add_header Access-Control-Allow-Methods 'GET, POST, OPTIONS';
        add_header Access-Control-Allow-Headers '*';

        # OPTIONS 预检
        if ($request_method = OPTIONS ) {
            add_header Content-Length 0;
            add_header Content-Type text/plain;
            return 204;
        }
    }
}
```