# 雨中冒险2 使用docker开服

[docker GitHub地址](https://github.com/avivace/ror2-server)  

由于开发商没有更新服务端，所有需要回退版本，直接pull上面github repo的docker server，server的版本是1.2.4.1。所以需要我们回退游戏本体版本。  

## 服务端docker compose示例

```yml
# docker-compose.yml
services:
  ror2server:
    image: avivace/ror2server:latest
    ports:
      - "27015:27015/udp"
    environment:
      - R2_PSW=PASSWORD
      - R2_PLAYERS=16
      - R2_HOSTNAME=YOUR SERVER NAME
    restart: unless-stopped
```

## 客户端回退版本

使用任意浏览器打开下面的网址以唤出steam客户端的控制台：  
```
steam://open/console
```

在steam控制台输入如下命令：  
```
download_depot 632360 632361 7660073450841700654
```

!!! Caution
    注意，在下载期间不会看到任何提示，不要关闭steam或休眠电脑等，在下载好后会出现这样的提示：`Depot download complete : "D:\Program Files (x86)\Steam\steamapps\content\app_632360\depot_632361" (1836 files, manifest 7660073450841700654) `

下载好先前的版本后，如希望steam能同步成就等，可以覆盖原游戏文件。若希望回到最新版本，检查游戏完整性或重下即可。不希望覆盖原文件可以 **添加非steam游戏** 。  

或者你可以使用我做得torrent下载旧版本。  
torrentid：8c9932dd983813912906a0956d3b1f2dfe141664

## 连接服务器

在雨中冒险2游戏中按下 **ctrl+alt+`** 唤出控制台，输入如下命令：  

```
cl_password "PASSWORD"; connect "<SERVER_IP>:PORT";
```

一般来说PORT都是27015。如果自行改过，请使用你自己设置的端口。没有密码是不需要前面一句命令及分号。  

## 其他

如需frp，请注意应当使用udp协议映射。