# 通过校园网使用宿舍网并科学上网指南（Xray）

## 情境描述

由于校园网存在高峰期不稳定的情况，现在需要利用校园网作为介质，以宿舍网作为出口。  

设想使用一个双网口设备，搭建一个v2ray（xray）节点在校园网和宿舍网。这样就可以通过代理客户端使用宿舍网。  

在此基础上，通过配置节点，还可以实现科学上网。  

同时，笔者还搭建了zerotier网络，为了在校园网满速使用zt里的nas，同样也可以使用这个节点达到目的。  

## 设备选用

这里使用了友善电子的Nanopi R2S。nanopi r2s正好有两个网口，足够使用了。  

系统使用的是友善电子官网的Debian，这样可以做到更细微的调整。  

## 网络路由

我们需要连接两个网络，这需要我们手动调整网络路由。  

我就读学校的校园网的网段是10.0.0.0/8，按照物理位置又划分成了不同的子网段，庆幸的是，各子网段之间是互通的。  

宿舍所在子网是 10.13.82.0/24，通过dhcp获得的网关为10.13.82.254。  

友善电子的这个Debian镜像使用的网络管理器是NetworkManager。下面我们需要针对需求，对路由进行修改。  

**首先**，需求如下：  
1. 所有流量出口走宽带，这里是我的eth0网口
2. 要能正常访问校内资源，即10.0.0.0/8网段
3. 关闭校园网ipv6，我目前只需要走宽带ipv6（直接关闭比较省事）

实现上述需求的具体操作如下：  
1. 关闭eth1（校园网）网卡默认路由
2. 建立10.0.0.0/8路由，网关10.13.82.254

命令如下：  
```bash
# 关闭该项默认路由
nmcli connection modify "Wired connection 2" ipv4.never-default yes
# 关闭ipv6
nmcli connection modify "Wired connection 2" ipv6.method ignore
# 添加路由和网关
nmcli connection modify "Wired connection 2" +ipv4.routes "10.0.0.0/8 10.13.82.254"
# 重启连接以生效
nmcli connection down "Wired connection 2" && sudo nmcli connection up "Wired connection 2"
```

## Xray节点配置

### Xray的安装

这里直接使用了这个一键安装脚本：[Github地址](https://github.com/233boy/Xray)  

**注意，这里有一个问题**，这个一键管理脚本在刚安装的时候是能用公网ipv6作为地址的，但是在查看/修改配置的时候，会因为没有公网ip而卡住。  

这里直接使用了默认配置。  

### 出口配置

接下来修改`config.json`，这个文件在`/etc/xray/config.json`,默认配置文件只有两个outbound，直连和阻塞。  

接下来，我们需要粘贴上我们自己的科学上网节点，并命名为`proxy`outbound。（这部分直接参照客户端某个节点的“导出配置到剪贴板”，然后将对应出口配置复制即可）  

整个`outbounds`修改好后大致如下：

![20250827142657](https://raw.githubusercontent.com/lyy1119/Imgs/main/img/20250827142657.png)

### 路由配置

路由部分在`routing`中，我们主要修改其中的`rules`部分。  

```json
"routing": {
        "domainStrategy": "IPIfNonMatch",
        "rules": [ ... ]
    }
```

`rules`的书写规则：  

一个`rule`的格式大致如下：  

```json
{
    "type": "field",
    "outboundTag": "direct",
    "marktag": "comments",
    "domain": [
        "geosite:cn",
        ...
        "geosite:category-games@cn"
    ]
},
```

其中`type`，都是`field`，不需要修改。`outboundTag`对应出口的其中一项。  

`marktag`用于标注，并无实际用途。  

`domain`还可以是`ip`，用于编写具体的目的地址。  

这样，目标就清晰很多了，按照需求编写相关路由即可。在文中就不展示相关内容了。  

不过除了按照域名和ip路由，xray还支持按照协议路由，可以做到阻塞bittorrent，或者将tcp、upd默认走直连或者代理。  
