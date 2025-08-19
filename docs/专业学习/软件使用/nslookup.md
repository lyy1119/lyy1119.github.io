# nslookup查看域名解析记录

在Windows和Linux下，都用命令行工具`nslookup`。这个工具可以用来查看计算机获取的域名解析记录。  

该工具可以很方便地排查相关网络问题。下面是主要的使用方法  

## 1.直接查询

```bash
nslookup domain.com
```

## 2.指定域名解析服务器

以域名服务器`1.1.1.1`为例。  

```bash
nslookup domain.com 1.1.1.1
```