# 更改时区和设置NTP同步

## 更改时区

```bash
# 查看当前时区
timedatectl

# 列出所有时区
timedatectl list-timezones

# 设置为上海时区
sudo timedatectl set-timezone Asia/Shanghai

```

## 设置NTP

1.安装chrony  

```bash
sudo apt install chrony   # Debian/Ubuntu
# 或 sudo yum install chrony  # CentOS/RHEL

```

2.修改ntp源  
在`/etc/chrony/sources.d`文件夹下，创建`.sources`后缀的文件，写入ntp服务器，如：  
```bash
server ntp.aliyun.com iburst
```

3.重新加载（重启）  
```bash
chronyc reload sources
```

之后在`timedatectl`命令输出中就能看到ntp状态了。  