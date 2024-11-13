# startx报错“Cannot open virtual console 1”

## 原因

1. 可能是用户没有添加到用户组`tty`中
2. 使用su切换到另一个用户运行`startx`也会导致该问题

## 解决方案

运行下面的命令将用户添加到tty用户组（不要用要添加的用户执行）  

```bash
usermod -a -G tty <username>
```

## 参考原文

[[SOLVED] xf86OpenConsole: Cannot open virtual console 1](https://bbs.archlinux.org/viewtopic.php?id=192329)