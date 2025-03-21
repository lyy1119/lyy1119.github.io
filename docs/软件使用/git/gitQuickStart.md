# git快速开始

## 1.添加用户信息

```bash
git config --global user.name lyy1119
git config --global user.email lyy2286301015@126.com
```

## 2.设置网络代理

请确保端口正确
```bash
git config --global http.proxy http://127.0.0.1:10809
git config --global https.proxy http://127.0.0.1:10809
```

## 3.存储鉴权

对于最新的git，已经不能使用密码鉴权，必须用ssh key或者token。为了避免每次都鉴权，可以在鉴权之前使用如下命令。  

**为了代码安全，请勿在公用电脑上保存鉴权**  

```bash
git config --global credential.helper store
```

## git查看现有配置

```bash
git config --list
```