# ufw对docker服务端口无效

## 原因

docker自动在防火墙列表中添加了开放端口的规则. 所以根本就没走到ufw端口就被放行了。  

## 解决方法

修改docker的配置文件`/etc/docker/daemon.json`(若没有就新建一个), 添加如下内容:  

```shell
{
  "iptables": false
}
```

重启docker  

```shell
systemctl restart docker
```