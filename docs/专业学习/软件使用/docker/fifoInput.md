# 创建FIFO实现向容器主进程控制台发送命令

对于类似Minecraft服务端的主进程，会自带一个控制台，这个控制台往往具有最高权限，能执行远程控制（如Rcon）等执行不了的命令。  

而一般开服，如使用`java -jar`直接运行程序，那么就无法使用这个控制台。  

解决方法很简单，创建一个`FIFO`管道即可，需要执行命令的时候使用`docker exec -i <containerName> sh -c 'echo "<command>" > <fifo pipe>'`即可。  


## Dockerfile

以构建Minecraft服务器为例：  

```dockerfile
FROM openjdk:21-jdk-slim

WORKDIR /minecraft

COPY . .
RUN chmod +x ./run.sh

COPY ./startup.sh ./startup.sh
RUN chmod +x ./startup.sh
# 运行命令
CMD ["/minecraft/startup.sh"]
```


主要在`run.sh`中，如下：  
```bash
#!/bin/bash
mkfifo /tmp/input
# 需要使用tail使输入绑定控制台进程
tail -f /tmp/input | java -Xms512M -Xmx512M -XX:+UseG1GC -XX:G1HeapRegionSize=4M -XX:+UnlockExperimentalVMOptions -XX:+ParallelRefProcEnabled -XX:+AlwaysPreTouch -XX:MaxInlineLevel=15 -jar velocity.jar
```

输出内容就无法直接显示了，需要使用`docker logs <container>`来查看