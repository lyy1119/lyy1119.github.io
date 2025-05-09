# nginx反向代理相关问题

可能出现使用nginx反向代理成`https`后无法访问的情况，需要将nginx的`config.php`修改`'overwriteprotocol' => 'http',`为`'overwriteprotocol' => 'https',`

## Reference
1. [nginx 进行 https 反向代理 nextcloud 后 APP 不能访问的解决办法-CSDN](https://blog.csdn.net/litte_frog/article/details/110296459)