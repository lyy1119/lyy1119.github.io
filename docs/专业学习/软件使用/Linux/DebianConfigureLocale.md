# Debian重新配置系统语言环境并安装中文字体

## 重新配置语言环境

```bash
sudo dpkg-reconfigure locales
```  

!!! info "提示"
    在dpkg-reconfigure的界面中，<kbd>Enter</kbd>键是确定，要修改选项使用<kbd>Space</kbd>。

## 安装中文字体

```bash
apt install ttf-wqy-zenhei
```