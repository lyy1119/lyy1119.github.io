# 6.动态路由技术

## 为什么需要动态路由

对于静态路由，如果网络拓扑发生改变，则管理员需要手动修改所有相关设备的路由表或网关。  

很明显，这对大型网络的维护和搭建是不现实的。故设计了动态路由协议，动态路由的本质是路由器之间相互“学习”，最终实现所有路由器都知道整个网络拓扑结构。  

## 动态路由的概念

动态路由是网络中路由器之间相互通信、更新自身路由表的这样一个过程。  

动态路由能实时适应网络拓扑变化，并调整自身路由表。   

## 动态路由的协议

### 1.RIP协议

RIP协议全称为Routing Information Protocal。  

RIP协议要求网络中各路由器都要记录并维护从它自身到其他每个网络的 **距离** 。  

!!! note
    距离不是指物理上的距离，而是在网络中经过的路由器个数。  

    其中直连网络，即路由器本地网络的距离定义为1。  

RIP协议会选择路径最短的进行报文的转发。即使这条路径十分繁忙。  

!!! note
    RIP协议仅适用于小型网络，当距离大于等于16时，认为是不可达到的。

使用RIP协议的路由器，会且仅会和相邻路由器交换信息。路由器之间交换信息的间隔是固定的。显然，随着网络规模的扩大，RIP协议造成的开销和占用也会增大。  

### 2.OSPF协议

OSPF协议的工作原理如下：

### 路由发现

### 路由选择

### 路由维护