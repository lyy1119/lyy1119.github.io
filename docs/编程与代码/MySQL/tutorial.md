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

## 2.创建表

**在数据库中创建一个表**  
```sql
CREATE TABLE <tableName> (
    <columnName> <dataType>,
    <columnName> <dataType>
);
```

如：  
```sql
CREATE TABLE employees (
    employee_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    hourly_pay DECIMAL(5 , 2),
    hire_date DATE
);
```

其中`VARCHAR(50)`中的数字50代表这个字符串最大长度50。`DECIMAL(5,2)`中的第一个数字5代表最大值，2代表小数点后位数。  

**选定table**  
```sql
SELECT * FROM <tableName>;
```

**重命名table**  
```sql
RENAME TABLE <originName> TO <newName>;
```

**删除table**  
```sql
DROP TABLE <tableName>;
```

**在table中添加列**  
```sql
ALTER TABLE <tableName>
ADD <columName> <dataType>;
```
**注意，第一行没有分号**  

**修改table中的列标题**
```sql
ALTER TABLE <tableName>
RENAME COLUMN <originColumnName> TO <newName>;
```