# 搭建Zerotier私有虚拟局域网指南

## 导航

原项目地址：[https://github.com/xubiaolin/docker-zerotier-planet](https://github.com/xubiaolin/docker-zerotier-plane)


| [搭建私有服务器](#搭建私有Planet服务器) | [将客户端加入网络](#将客户端加入网络) |

## 搭建私有Planet服务器

在服务器上安装以下软件：  
- git
- docker

克隆项目代码：
```bash
git clone https://github.com/xubiaolin/docker-zerotier-planet.git
```

cd进入目录并运行部署脚本：
```bash
cd docker-zerotier-planet
./deploy.sh
```

根据提示来选择即可，操作完成后会自动部署  
```
欢迎使用zerotier-planet脚本，请选择需要执行的操作：
1. 安装
2. 卸载
3. 更新
4. 查看信息
5. 退出
请输入数字：
```

根据提示放行相应端口即可。  

根据提示，下载`planet`文件。`planet`文件将在客户端连接网络时用到。  

根据提示进入服务端网页配置页面。  

使用默认账号为:admin  

默认密码为:password  

点击`Add network`添加网络，点击`detail`进入详情页面，可以看到网络id。新建的网络没有路由规则，点击`Easy setup`，点击`Generate network address`快速建立一个路由规则。点击`submit`确定即可。

## 将客户端加入网络

### Windows端

复制下载的`planet`文件到`C:\ProgramData\ZeroTier\One`，以覆盖文件。  

`Win + R`，输入`services.msc`进入服务页面，找到`ZeroTier One`，点击重启服务，以使用新的`planet`文件。  

右击Windows图标，点击`Powershell 管理员`，输入如下命令加入网络：  
```bash
zerotier-cli.bat join <网络id>
```

看到`200 join OK`就代表加入成功。

加入成功后需要登陆服务端管理界面的相应网络，勾选`Authorized`。

### Linux端



### MacOS端

### Android端