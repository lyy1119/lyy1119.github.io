# Docker清理

docker有命令可以自动清理未使用的镜像、容器、网络和缓存等资源：  
```bash
docker system prune # -a 清除所有未使用的资源
```

## 更精细的清理

### 清理未使用的镜像

```bash
docker image prune # -a 清除所有未使用的镜像
```

### 清理未使用的container

```bash
docker container prune
```

### 清理未使用的volume

```bash
docker volume prune
```

### 清理未使用的网络

```bash
docker network prune
```