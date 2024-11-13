# docker换源教程

## 临时直接使用另一个源

假如换的源地址为`dockerpull.org`。  
在pull镜像时使用如下命令即可：  
```bash
docker pull dockerpull.org/hello-world
```

## 永久换源

docker的配置文件默认在`/etc/docker/daemon.json`。  
编辑上面这个配置文件即可。  

配置文件示例：  
```json
{
    "registry-mirrors": [
    	"https://docker.unsee.tech",
        "https://dockerpull.org",
        "docker.1panel.live",
        "https://dockerhub.icu"
    ]
}
```

## 可用镜像源

1. [目前国内可用Docker镜像源汇总](https://www.coderjia.cn/archives/dba3f94c-a021-468a-8ac6-e840f85867ea)  
2. [docker国内镜像加速列表](https://xuanyuan.me/blog/archives/1154)