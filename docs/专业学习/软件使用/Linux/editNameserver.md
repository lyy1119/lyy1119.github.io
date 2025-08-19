# 修改Linux使用的Dns服务器

## 1.临时修改

直接编辑`/etc/resolv.conf`  

```
nameserver 8.8.8.8 #修改成你的主DNS地址
nameserver 8.8.4.4 #修改成你的备用DNS地址
```

注意，上述修改会在重启后失效


## 2.修改网卡的dns

需要重启网络服务以生效

## 来源&参考

1. [几个修改Linux服务器DNS地址的方法汇总](https://www.itbulu.com/change-linux-dns.html)