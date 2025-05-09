# rdesktop连接Windows远程桌面

Linux下可以使用rdesktop连接Windows的远程桌面。

## 安装

```bash
sudo apt install rdesktop
```

## 参数

| 参数 | 意义 |
|---|---|
|-g|指定分辨率，比如`-g 1920x1080`、`-g workarea`即最大化|
|-u|指定用户名，`-u admin`|
|-p|指定密码，`-p passwd`|
|-f|全屏模式，可使用Ctrl+Alt+Enter组合键退出全屏|
|-r disk:share_name=/local-disk |将本地磁盘映射到远程电脑，其中share_name为显示名称，可自定义，local-disk表示本地linux的一个目录，比如 /data|
|-r clipboard:PRIMARYCLIPBOARD| 允许在远程主机和本机之间相互共享剪切板|
|-r sound:off|关闭声音|
|-r sound:on|开启声音|
|-P|启用位图缓存|
|-z|启用RDP数据流压缩|

示例：
```bash
rdesktop -g workarea -P -z -r clipboard:PRIMARYCLIPBOARD -u windowsuser 192.168.31.100:3389 -u password
```

## 其他问题

如果遇到剪切板功能不正常，可以重启远程Windows的`rdpclip.exe`。  

## Reference

1. [rdesktop命令详解-百度经验](https://jingyan.baidu.com/article/295430f1c8798a0c7e00502a.html#:~:text=3%E3%80%81-r%20clipboard%3APRIMARYCLIPBOARD%20%E5%85%81%E8%AE%B8%E5%9C%A8%E8%BF%9C%E7%A8%8B%E4%B8%BB%E6%9C%BA%E5%92%8C%E6%9C%AC%E6%9C%BA%E4%B9%8B%E9%97%B4%E5%85%B1%E4%BA%AB%E5%89%AA%E5%88%87%E6%9D%BF%EF%BC%8C%E5%B0%B1%E6%98%AF%E5%8F%AF%E4%BB%A5%E5%A4%8D%E5%88%B6%E7%B2%98%E8%B4%B4%E3%80%82,%E4%BB%A5%E4%B8%8A%E6%98%AFrdesktop%E7%9A%84%E5%B8%B8%E7%94%A8%E5%8F%82%E6%95%B0%EF%BC%8C%E6%9B%B4%E5%A4%9A%E5%8F%82%E6%95%B0%E8%AF%B7%E8%87%AA%E8%A1%8C%E7%99%BE%E5%BA%A6%E6%88%96%E8%80%85%E5%9C%A8linux%E4%B8%AD%E6%89%A7%E8%A1%8C%20rdesktop%20--help%E6%9F%A5%E7%9C%8B%E3%80%82)
2. [Linux和Windows间的远程桌面访问-CSDN](https://blog.csdn.net/fuhanghang/article/details/143759755)
3. [Cannot cut and paste from Ubuntu Gutsy and Edgy to Windows (of any version)-bugs.launchpad.net](https://bugs.launchpad.net/ubuntu/+source/rdesktop/+bug/175964)
4. [rdesktop共享剪贴板的问题](https://blog.csdn.net/weixin_33895604/article/details/94150725)