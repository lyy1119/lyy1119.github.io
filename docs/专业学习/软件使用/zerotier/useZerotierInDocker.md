# 通过docker部署zerotier Linux客户端

## docker-compose.yml

```yml
services:
  zerotier:
    image: zerotier/zerotier:1.14.1  # 使用指定版本
    container_name: zerotier
    restart: unless-stopped
    network_mode: "host"
    privileged: true
    volumes:
      - /var/lib/zerotier-one:/var/lib/zerotier-one
    environment:
      - ZT_NETWORK=your_network_id_here
    cap_add:
      - NET_ADMIN
      - SYS_ADMIN
```

## 使用：

加入网络：  
```bash
docker exec -it zerotier zerotier-cli join your_network_id_here
```

检查状态:  
```bash
docker exec -it zerotier zerotier-cli status
```