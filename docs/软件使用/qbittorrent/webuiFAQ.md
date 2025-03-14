# qbittorrent webui使用的若干问题

## 1.docker搭建的qbittorrent webui访问出现unauthorized

注意docker在映射端口的时候，container内部和宿主机的端口需要相同，比如`8080:8080`。  

## 2.webui 设置邮件题型点测试没用

如果你确信你的账号、授权码和服务器地址没有问题的话，检查你在点击测试前是否点了保存。  