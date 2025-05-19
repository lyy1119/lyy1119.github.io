# docker-compose.yml中build image部署

docker-compose部署服务时可以不需要提前载入（load）镜像（image），对于自己打包的服务，如果原文件很小或者打包后镜像太大，不便于传输，可以在`docker-compose.yml`中使用`build`关键字来说明这个image需要现场build。  

## docker-compose.yml 写法

假设你在和`docker-compose.yml`同级目录下有一个用于构建镜像的`Dockerfile`。  

```yml
services:
    <name>:
        build:
            context: . # Dockerfile所在目录
            dockerfile: Dockerfile # 指定Dockerfile名称
        # 剩下的都一样，主要区别是用build替代image
        networks:
            - ...
        volumes:
            ...
        ...
```