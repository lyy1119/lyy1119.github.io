# 使用scrutiny docker的若干问题

## 我的docker-compose.yml

```yml
services:
  scrutiny:
    container_name: scrutiny
    image: ghcr.io/analogj/scrutiny:master-omnibus
    cap_add:
      - SYS_RAWIO
      - SYS_ADMIN
    restart: unless-stopped
    ports:
      - "8081:8080" # webapp
      - "8086:8086" # influxDB admin
    volumes:
      - /run/udev:/run/udev:ro
      - /opt/scrutiny/config:/opt/scrutiny/config
      - /opt/scrutiny/influxdb:/opt/scrutiny/influxdb
    devices:
      - "/dev/nvme0:/dev/nvme0"
    environment:
      - SCRUTINY_SCRUTINIZE=true
```

## 1.关于nvme硬盘不显示的问题

nvme硬盘应在devices中这样写： `/dev/nvme0` 而不是 `/dev/nvme0n1` 或者 `/dev/nvme` 或者 `/dev/nvme0n1p1` 。  