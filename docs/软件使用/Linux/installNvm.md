# 安装nvm

[nvm项目地址-github](https://github.com/nvm-sh/nvm)  

## 使用curl或者wget从脚本安装

```bash
# curl
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
# wget
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
```

剩下的github上的`README`有指引。  

## 安装特定node版本与使用

```bash
# 安装node版本，如16
nvm insatll 16
# 使用
nvm use 16

# 之后可以直接使用node命令，其版本就是use后版本号的版本
```