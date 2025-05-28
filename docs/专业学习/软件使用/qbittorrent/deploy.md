# 在服务器上部署qbittorrent webui

## 1.安装qbittorrent

```bash
# 添加软件源并安装
sudo add-apt-repository ppa:qbittorrent-team/qbittorrent-stable
sudo apt update
sudo apt install qbittorrent-nox  # 无GUI版本（适合服务器）
```

## 2.编写service文件

```ini
[Unit]
Description=qBittorrent-nox service
After=network-online.target

[Service]
ExecStart=/usr/bin/qbittorrent-nox # --webui-port=9090 使用这个参数在启动时固定端口
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

将service复制到`/etc/systemd/system/`下，然后执行  
```bash
sudo systemctl daemon-reload
sudo systemctl start qbittorrent
sudo systemctl enable qbittorrent
```
以启动服务。  

## 3.访问 Web 界面
- 浏览器访问 http://服务器IP:8080  
- 默认账号：admin，默认密码：adminadmin（首次登录后需修改）。

注意，需要放行相应端口8080，和下载、上传端口（见qbittorrent的相关设置）

其他设置在webui界面完成。  