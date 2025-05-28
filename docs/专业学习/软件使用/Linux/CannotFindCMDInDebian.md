# Debian找不到apt安装的软件

## 原因

Debian默认没有将`/usr/sbin`和`/sbin`添加到环境变量`PATH`中。

## 临时解决方法

在命令行输入以下命令将上述路径添加到环境变量。  
```bash
export PATH=$PATH:/usr/sbin::/sbin
```

## 永久解决方法

对**用户**的终端配置文件`.bashrc`添加下面的代码:  
```bash
export PATH=$PATH:/usr/sbin::/sbin
```  

然后加载一遍`.bashrc`  
```bash
source ~/.bashrc
```