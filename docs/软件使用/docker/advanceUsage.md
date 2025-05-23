# docker的高级用法

## Dockerfile在构建时使用参数

在使用`docker-compose.yml`的`build`指定从`Dockerfile`构建镜像时，可以通过在`docker-compose.yml`中的`build.args`设置的参数来影响`Dockerfile`。  

如，  
```Dockerfile title="Dockerfile"
# 使用传入的 BASE_IMAGE 参数作为基础镜像
ARG BASE_IMAGE=python:3.10-slim
FROM ${BASE_IMAGE}

# 定义一个控制下载的参数
ARG DOWNLOAD_TOOL=false

RUN echo "Using base image: ${BASE_IMAGE}"

# 根据参数选择是否下载某个工具
RUN if [ "$DOWNLOAD_TOOL" = "true" ]; then \
      curl -o /usr/local/bin/tool https://example.com/tool && chmod +x /usr/local/bin/tool; \
    fi

```

```yml title="docker-compose.yml"
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
      args:
        BASE_IMAGE: python:3.11-slim
        DOWNLOAD_TOOL: "true"

```