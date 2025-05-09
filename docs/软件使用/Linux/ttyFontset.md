# tty下字体调整

对于某些高分辨率或小尺寸的屏幕，Linux tty下的字体可能非常小。这可以通过设置tty字体解决。  

下面的经验是根据笔者使用Debian和Arch Linux所写的，可能不完全适用所有发行版。  

## 查看可用字体

```bash
ls /usr/share/consolefonts
```

对于过大的屏幕，现有字体可能还是太小，可用使用如下命令安装大小更多的字体  
```bash
# arch 安装Terminus字体
pacman -S terminus-font
# debian可能需要从网站下载
```

## 临时设置

```bash
setfont <font name> # 字体名是不加.pfs.gz后缀的
```

## 永久设置

!!! warning
    下面的内容可能仅使用Debian

```bash
sudo vim /etc/default/console-setup
```

修改其中的`CODESET`、`FONTFACE`、`FONTSIZE`。  
`CODESET`、`FONTFACE`、`FONTSIZE`来自字体名，一般字体名写作`<CODESET>-<FONTFACE><FONTSIZE>`。

## Reference
1. [linux命令行界面字体调整-Worklite](https://worktile.com/kb/ask/459382.html)