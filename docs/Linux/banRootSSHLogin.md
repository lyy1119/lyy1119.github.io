# 禁止root用户通过ssh远程登陆


## 1.修改ssh的配置文件

ssh的配置文件为：`/etc/ssh/sshd_config`  

将配置文件中的`PermitRootLogin yes`改为`PermitRootLogin no`即可，没有前者的话自己写一行后者内容即可。  

## 2.重启sshd服务

!!! warning "注意"
    需要sudo权限

```bash
systemctl restart sshd
```