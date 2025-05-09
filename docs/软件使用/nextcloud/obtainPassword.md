# 重新获取密码

如果忘记了Nextcloud的密码，可以通过如下命令获取  
```bash
sudo docker exec <nextcloud-aio-mastercontainer name> grep password /mnt/docker-aio-config/data/configuration.json
```

## Reference
1. [How to re-obtain/retreive the Nextcloud AIO passphrase?-github issue](https://github.com/nextcloud/all-in-one/discussions/1786)