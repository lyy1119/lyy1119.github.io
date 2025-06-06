# 5.路由技术

不同网络或网段的主机需要通过路由器（或者三层交换机）来通信。  

## 网关 Gateway

是一个网络接连到另一个网络的“关口”。  

任何一个ip地址都可以是网关地址。  

## 下一跳

下一跳是指当前路由条目为到达目的地址而发往的下一个路由器这一动作。下一跳ip即下一个网关的ip。  

路由表：存储着其他目标网络地址、子网掩码、网关地址（即下一跳地址）的条目。  


## 网段间的设置

当不设置网关时，所有主机只能与同网段的主机通信，即使物理上连接了路由器（其实在之前提到过，路由器上其实有一个交换机，也就是二层交换机）。

### 西门子系列三层交换机路由设置

#### 本地路由

即子网间路由。  

情景：目前有多台主机，一个三层交换机。其中各主机分成了两个网段，并均与三层交换机通过网线物理直连。需要配置三层交换机的路由功能来支持不同网段的访问。  

西门子系列的工业三层交换机需要启用vlan才能支持子网路由功能。  

**步骤**：  
1. 启动vlan并将不同网段的端口分配至不同vlan
2. 在子网页面，为未分配网段地址的vlan设置ip及掩码
3. 通过网络，配置相同网段的主机的网关
4. 连接到与pc不同网段的主机，手动设置网关
5. 测试ping通信

#### 静态路由

静态路由是指两台具有路由功能的设备之间的路由通信。  

<div align=center>  <!--使整体居中-->
    <div style="width: 50%;">			<!--块级封装-->
        <center>	<!--将图片和文字居中-->
        <img src="https://raw.githubusercontent.com/lyy1119/Imgs/main/img/20250607124745.png"
            alt="图片无法加载，请检查网络连接"/>
        <br>		<!--换行-->
        <div style="font-size: 12px;font-style:italic;">
            网络拓扑及vlan划分
        </div>	<!--标题-->
        </center>
    </div>
</div>

显然，对于这种设备的静态路由，需要设置三个网段，而不同网段需要不同vlan，进而需要划分三个vlan。  

对于PC机，其下一跳是图中的`192.168.1.1`，对于`192.168.2.1`其下一跳是`192.168.1.2`。  

注意，两个路由设备之间的vlan需要相同，不然无法通信。  

