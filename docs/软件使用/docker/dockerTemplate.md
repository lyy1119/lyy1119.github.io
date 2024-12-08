# 我的Dockerfile模板

```Dockerfile
# 基础镜像
FROM <image>:<tag>
# 设置时区 上海
RUN ln ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' > /etc/timezone
# 工作目录
WORKDIR <workdir>
# 复制文件
COPY <src> <dest>
# 安装依赖 apt-get pacman...
RUN <command>
# 运行命令
RUN <command>
```