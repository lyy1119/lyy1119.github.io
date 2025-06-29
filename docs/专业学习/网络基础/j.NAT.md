# 10.NAT技术

NAT，即Network Address Translation。  

NAT技术的主要应用是内部网络主机访问外部网络。NAT技术解决了Ipv4下地址不够的问题，但是，很显然，使用NAT技术，外部主机（拥有公网Ip的主机）主动访问内部网络主机会更麻烦。  

当具有公网Ip的路由器下的主机访问外部网络主机时，从数据包来看，在路由器和外部网络主机之间，数据包中的源地址和目的地址是路由器或者外部网络主机地址。也就是，在外部网络主机看来，这个通信是和路由器之间进行的。  

当数据包到达路由器时，路由器将对数据包中的源或者目的地址替换为内部主机地址，以实现外部网络与内部网络之间的通信。  

显然，对于外部网络主机，内部网络是不可见的。这不仅解决了Ipv4不够的问题，也增强了内部网络的安全性。  

## 相关名词

**NAT表** ： 当内部网络中有多台主机访问外部网络时，为了防止流量之间的混乱而建立的一个映射表。  


## 静态NAT

在静态NAT中，一个内网IP将会被对应转换为一个公网IP，即两者是一一对应的。  

## 动态NAT

在动态NAT中，路由器上设置有一个地址池，地址池内有一个或多个公网IP。内网主机将动态地使用其中的地址作为转换的IP。  

在同一时间，只能有有限个映射存在。当地址池中的地址都使用完了，其他主机就必须等待现有连接解除，从而释放ip给其他主机使用。  

## NAPT

NAPT在NAT的基础上增加了端口转换，即多个主机可以使用一个ip的多个端口进行通信，极大地解决了动态NAT中ip占用的问题。  


