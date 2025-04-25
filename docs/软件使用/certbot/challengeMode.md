# Challenge模式申请证书

challenge模式申请证书能避开防火墙限制，也就是无论是否能访问通，都可以申请证书。不够也有缺点：只能手动刷新证书。  

| [原文连接](https://blog.csdn.net/davenian/article/details/146078319) |  

## 指定challenge模式申请证书

```bash
sudo certbot certonly --manual --preferred-challenges dns -d <you.domain>
```

或者不指定域名，让certbot自动检测  
```bash
sudo certbot certonly --manual --preferred-challenges
```

## 创建TXT DNS记录

执行`preferred-challenges`后，会看到提示，让你创建一个指定域名的TXT DNS记录，在DNS解析中创建即可，不过和其他域名解析一样，需要等待生效。在生效前，不要继续certbot。  

你可以使用以下bash语句来检测：  
```bash
while true; do dig <domain.specific> TXT +short; date; sleep 2; done
```

直到看到返回指定txt内容。就可以继续了。  

## 其他

证书3月一换，需要手动重复上述操作。  