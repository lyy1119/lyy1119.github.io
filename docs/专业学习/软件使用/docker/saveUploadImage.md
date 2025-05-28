# 保存和上传镜像文件

## 保存镜像到本地文件

```shell
docker save -o <fileName> <imageName>
```

## 从本地镜像文件上传

```shell
docker load -i <fileName>
```