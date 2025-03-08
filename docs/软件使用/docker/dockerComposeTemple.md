# docker-compose.yml模板与解释

```yml
services:
  my_service:
    image: my_image:latest  # 替换为你的镜像名称
    container_name: my_container  # 自定义容器名称
    ports:
      - "8080:80"  # 将宿主机端口 8080 映射到容器内部端口 80
    volumes:
      - my_volume:/app/data  # 绑定命名卷到容器内的 /app/data 目录
      - ./config:/app/config  # 绑定本地目录到容器内的 /app/config 目录
    restart: unless-stopped  # 设定容器的重启策略
    environment:
      - TZ=Asia/Shanghai  # 设置时区，可按需修改

volumes:
  my_volume:  # 定义一个命名卷
```