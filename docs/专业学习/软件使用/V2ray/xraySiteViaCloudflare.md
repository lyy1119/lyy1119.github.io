# 利用Cloudflare搭建Xray（V2ray）节点

## 情境描述

在搭建自己的vpn节点的时候，即使使用流量伪装，也可能被墙。  

我们可以使用Cloudflare的cdn加上Xray的xhttp伪装在一定程度上避免被墙。  

!!! note
    为什么使用xray？  
    在v2ray的某个版本之后，某些客户端似乎不再支持v2ray的http伪装。

## 步骤

1. [下载Xray一键脚本](https://github.com/233boy/Xray)到服务器并安装
2. 登陆cloudflare，先解析不带cdn的域名到服务器
3. 更改服务器协议和伪装类型为xhttp
4. 在cloudflare开启伪装