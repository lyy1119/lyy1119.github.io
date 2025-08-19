# Nextcloud Linux客户端开启虚拟文件夹

Linux下的虚拟文件夹目前还在实验阶段，但是还是可以开启的。  

在安装好客户端后，在这个目录`/home/yourusername/.config/Nextloud/`下可以找到名为`nextcloud.cfg`的文件。  

在`[General]`下添加`showExperimentalOptions=true`这一行，然后重启Nextcloud客户端，就可以在UI中发现 *实验性选项* ，开启后就可以使用虚拟文件（夹）功能。  

## 参考

1. [[Nextcloud官方论坛]Virtual Files on Ubuntu Desktop](https://help.nextcloud.com/t/virtual-files-on-ubuntu-desktop/124668)