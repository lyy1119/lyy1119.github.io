# systemctl添加自定义服务

## 1.编写service文件

## 2.将service文件复制到系统中service文件存储的位置

将service文件复制到系统中service文件的存储位置：  
```bash
cp xxx.service  /usr/lib/systemd/system/xxx.service
```

## 3.运行服务及设置服务开机启动

- 运行服务  

```bash
systemctl start xxx #xxx为你拷贝后的文件的文件名前缀
```

- 查看服务状态  

```bash
systemctl status xxx
```

- 停止服务  

```bash
systemctl stop xxx
```

- 设置/取消服务开机自启动

```bash
systemctl enable xxx
systemctl disable xxx
```