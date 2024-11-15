# ufw对docker服务端口无效

## 原因

docker自动在防火墙列表中添加了开放端口的规则. 所以根本就没走到ufw端口就被放行了。  

## 解决方法

一下有删除线的是错误做法（指单纯关闭`iptables`），设置`"iptables": false`[会中断 docker-compose 的 DNS 发现](https://jueee.github.io/docker-doc/about-docker-iptables-false.html)。  

从而导致docker内程序无法访问其他同网络的docker服务 **甚至不能访问外部主机连接的互联网** 。  

~~修改docker的配置文件`/etc/docker/daemon.json`(若没有就新建一个), 添加如下内容:~~  

```shell
{
  "iptables": false
}
```

~~重启docker~~  

```shell
systemctl restart docker
```


**正确的解决方法** 是：对于内部服务container，去掉docker-compose.yml端口映射即可，去掉后只是外网无法访问这个服务，但是同一docker网络下的别的容器依然能访问。  
或者参照[这个解决方法](https://jueee.github.io/docker-doc/about-docker-iptables-false.html)。  