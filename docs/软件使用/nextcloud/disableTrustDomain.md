# 取消信任域设置

!!! warning
    取消信任域设置将对您的数据安全产生严重潜在风险，若无必要，请不要这样做

要“取消”信任域设置，需要修改`config/config.php`。  
修改其中的`trust-domains`如下：
```php
'trusted_domains' => array(
     ...
     <index>=>preg_match('/cli/i',php_sapi_name())?'127.0.0.1':$_SERVER['SERVER_NAME'],
), // index是array的序列，按照顺序写就行
```

或者  
```php
'trusted_domains' => array(
     0 => $_SERVER['HTTP_HOST'],
),
```

## Reference
1. [Nextcloud允许不被信任的域访问 取消 trusted domains-博客园](https://www.cnblogs.com/jsrd/p/17488223.html)