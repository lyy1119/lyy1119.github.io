# MySQL笔记

mysql的语句关键词是 **大小写不敏感的** 。  

## 1.Database的创建与删除

**创建一个database**  
```sql
create database <databaseName>;
```

**选中某个database**  
```sql
use <databaseName>;
```

**删除database**  
```sql
drop database <databaseName>;
```

**设置database只读**  
```sql
alter database <dbName> read only = 1;
```

当数据库被设置成只读时，数据库不能修改和删除。  

