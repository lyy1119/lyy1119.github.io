# 基于docker的快速开服image

适用于Minecraft `1.17`及以上，`1.20.5`及以下。  

可以通过更改基础镜像openjdk的版本来实现`1.17`以下或`1.20.5`及以上。  

## Dockerfile

```Dockerfile
# 基础镜像
FROM openjdk:17-jdk-slim
# 设置时区 上海
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' > /etc/timezone
# 工作目录
WORKDIR /minecraft
# 复制文件
COPY ./startup.sh /minecraft/startup.sh
RUN chomod +x /minecraft/startup.sh

# 安装vim方便修改
RUN apt-get update && \
    apt-get install -y --no-install-recommends vim && \
    apt-get install -y --no-install-recommends curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# eula
RUN echo "eula=true" >> /minecraft/eula.txt
# 运行命令
CMD ["/minecraft/startup.sh"]
```

### startup.sh

```bash
#!/bin/bash

set -e

# 默认值
CORE_URL="${CORE_URL:-}"
MIN_RAM="${MIN_RAM:-1G}"
MAX_RAM="${MAX_RAM:-2G}"
JAR_NAME="server.jar"
JVM_ARGS_FILE="jvm.args"

# 下载 server.jar（如果不存在）
if [ ! -f "$JAR_NAME" ]; then
    if [ -n "$CORE_URL" ]; then
        echo "Downloading Minecraft core from $CORE_URL..."
        curl -o "$JAR_NAME" -L "$CORE_URL"
    else
        echo "Error: server.jar not found and CORE_URL is not provided."
        exit 1
    fi
else
    echo "$JAR_NAME already exists, skipping download."
fi

# 写入 JVM 参数文件
echo "-Xms$MIN_RAM" > "$JVM_ARGS_FILE"
echo "-Xmx$MAX_RAM" >> "$JVM_ARGS_FILE"

# 启动 Minecraft 服务端
echo "Starting Minecraft server..."
exec java $(cat $JVM_ARGS_FILE) -jar "$JAR_NAME" --nogui
```

## docker-compose.yml

```yml
services:
  minecraft:
    image: minecraft-easysetup
    container_name: minecraftserver
    environment:
      - CORE_URL=https://api.papermc.io/v2/projects/paper/versions/1.18.2/builds/388/downloads/paper-1.18.2-388.jar  # 替换为实际地址
      - MIN_RAM=1G
      - MAX_RAM=1G
    restart: unless-stopped
    volumes:
      - /opt/Minecraft/lobby/world:/minecraft/world
      - /opt/Minecraft/lobby/mods:/minecraft/mods
      - /opt/Minecraft/lobby/backups:/minecraft/backups
      - mcserver_1:/minecraft
    networks:
      - mcnet

# 记得创建网络：用于群组服务器
# docker network create mcnet
networks:
  mcnet:
    external: true

volumes:
  mcserver_1:
```

## 构建

```bash
docker build -t minecraft-easysetup .
```