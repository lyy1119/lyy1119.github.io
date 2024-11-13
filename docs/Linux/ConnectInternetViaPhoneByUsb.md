# linux/debian 通过USB连接手机热点



## 1.查看新增的端口名称  

在插入usb前后执行以下命令。  
```bash
ip a
```
## 2.改变网络使用的端口
```bash
dhclient <xxx>
#xxx为多出来的端口名，可以使用tab补全
```