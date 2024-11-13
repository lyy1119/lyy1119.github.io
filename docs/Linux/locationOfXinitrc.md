# .xinitrc模板文件的位置

`/etc/X11/xinit/xinitrc`  

!!! warning "注意"
    第一次写用户的.xinitrc时，可以cp模板文件，然后修改。模板文件默认启动一个简易的桌面环境，需要注释掉。

.xinitrc模板文件内容如下：  
```bash
#!/bin/sh

# /etc/X11/xinit/xinitrc
#
# global xinitrc file, used by all X sessions started by xinit (startx)

# invoke global X session script
. /etc/X11/Xsession #这一行需要注释点，然后写你的启动脚本
```