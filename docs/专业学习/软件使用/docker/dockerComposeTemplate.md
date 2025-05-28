# docker-compose.yml模板

以下是一个尽可能**全面**的 `docker-compose.yml` 模板，涵盖了常见的部署情况，如：

* 容器构建（使用 `image` 和 `build` 两种方式）
* 端口映射
* 环境变量
* 卷挂载
* 网络
* 依赖服务（`depends_on`）
* 容器重启策略
* 日志配置
* 健康检查
* 命令与入口点覆盖

## ✅ 模板一：使用 `image` 的部署方式

```yaml
version: '3.9'

services:
  app:
    image: your-image-name:latest
    container_name: your-app
    ports:
      - "80:80"
      - "443:443"
    environment:
      - APP_ENV=production
      - DATABASE_URL=mysql://user:password@db:3306/app
    volumes:
      - ./app:/usr/src/app
      - app-data:/data
    restart: unless-stopped
    depends_on:
      - db
      - redis
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost"]
      interval: 30s
      timeout: 10s
      retries: 5
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
    networks:
      - frontend
      - backend

  db:
    image: mysql:8.0
    container_name: mysql-db
    environment:
      - MYSQL_ROOT_PASSWORD=yourpassword
      - MYSQL_DATABASE=app
    volumes:
      - db-data:/var/lib/mysql
    ports:
      - "3306:3306"
    restart: unless-stopped
    networks:
      - backend

  redis:
    image: redis:7
    container_name: redis-cache
    ports:
      - "6379:6379"
    volumes:
      - redis-data:/data
    restart: unless-stopped
    networks:
      - backend

volumes:
  db-data:
  app-data:
  redis-data:

networks:
  frontend:
  backend:
```

## ✅ 模板二：使用 `build` 本地构建镜像方式

```yaml
version: '3.9'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
      args:
        BUILD_ENV: production
    container_name: your-app
    ports:
      - "80:80"
    environment:
      - APP_ENV=production
    volumes:
      - ./app:/usr/src/app
    depends_on:
      - db
    restart: always
    networks:
      - backend

  db:
    image: postgres:16
    container_name: postgres-db
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=secret
      - POSTGRES_DB=mydb
    volumes:
      - pg-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    networks:
      - backend

volumes:
  pg-data:

networks:
  backend:
```

## ✅ 补充说明（部署选项汇总）

| 选项            | 功能解释                                     |
| ------------- | ---------------------------------------- |
| `image`       | 使用已有镜像部署，一般来说对于一个<app>，`image`和`build`二选一      |
| `build`       | 从 Dockerfile 构建镜像部署                      |
| `ports`       | 端口映射：宿主机:容器，不暴露端口的就不需要，相同`networks`的容器可以通过容器名互相访问服务|
| `environment` | 设置环境变量，是可选的，这里设置的环境变量会体现在容器内的`bash`环境变量中，部分镜像依赖这个功能做初始化|
| `volumes`     | 数据持久化或代码挂载，可选的，要做持久化数据必备，也可以将容器内文件映射到宿主机|
| `depends_on`  | 服务依赖关系，可选的|
| `restart`     | 自动重启策略（如 `no`、`always`、`unless-stopped`）|
| `healthcheck` | 健康检查配置，可选的|
| `networks`    | 自定义网络，适用于微服务，对于多服务（如前后端、数据库）尤为重要|
| `logging`     | 日志驱动与配置，可选的|
| `command`     | 覆盖容器默认命令，可选的，一般不配置|
| `entrypoint`  | 覆盖默认入口点，可选的，一般不配置|
