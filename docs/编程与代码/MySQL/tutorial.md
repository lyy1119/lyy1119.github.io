# MySQL笔记

mysql的语句关键词是 **大小写不敏感的** 。  
mysql语句以分号作为一句话的结束，所以根据个人习惯，可以将一行语句分成多行书写。  

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

**修改列的数据类型**
```sql
ALTER TABLE <tableName>
MODIFY COLUMN <columnName> <dataType>;
```

**移动列的顺序**
```sql
ALTER TABLE <tableName>
MODIFY <column1Name> <dataType>
AFTER <column2Name>;
```
将列1移动到列2的右侧。  

**将某列移动到首列**
```sql
ALTER TABLE <tableName>
MODIFY <columnName> <dataType>
FIRST;
```

**删除某列**
```sql
ALTER TABLE <tableName>
DROP COLUMN <columnName>;
```

## 3.插入数据（在表中插入行）

**插入一行数据**
```sql
INSERT INTO <tableName>
VALUES (...);
```
在括号中写入一行中每列的内容。注意每列的数据格式，输入值要和数据格式对应，每列之间用 **逗号** 隔开。  

如：  
```sql
INSERT INTO employees
VALUES (1 , "LIN" , "Y" , 25 , "2025-04-13");
```

**一次插入多行**
```sql
INSERT INTO <tableName>
VALUES () , () , () , ();
```

**仅插入部分数据（部分列）**
```sql
INSERT INTO <tableName> (columnName1 , columnName2)
VALUES (value1 , value2);
```
上述语句仅插入表的`columnName1`和`columnName2`列的数据。  

## 4.查看数据

**选定/查看table的所有列**  
```sql
SELECT * FROM <tableName>;
```

**选定/查看table的特定列**
```sql
SELECT <colName1> <colName2>
FROM <tableName>;
```
列名不是必须按照表中的左右的，可以交换

**查看特定行**
```sql
SELECT * FROM <tableName>
WHERE <columnName> = <value you want>;
```
实际上`=`是一个操作符，会返回为true的行，所以可以这样写。  

```sql
SELECT * FROM <table>
WHERE hourly_pay >= 0;
```

## 5.更改与删除行

**更改某行的某列**
```sql
UPDATE <tableName>
SET <columnName> = <value>
WHERE <columnName2> = <value2>;
```
上述语句将表`tablename`中列`columnname2`的值为`value2`的行的`columnName`列数据更改为`value`。  

!!! Note
    如果使用上述语句更改行的某列的值出现以下报错：  
    `You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column.`  
    是因为当前指定的WHERE column的column不是索引键`key column`  
    解决方法：  
    使用如下命令将列设置为索引键或者主键  
    ```sql
    -- 添加索引
    ALTER TABLE employees ADD INDEX (employee_id);
    -- 设置为主键
    ALTER TABLE employees ADD PRIMARY KEY (employee_id);
    ```

如果要改变某特定行的多列值，可以这样写：
```sql
UPDATE <tableName>
SET <column1> = <value1>,
    <column2> = <value2>
WHERE <column3> = <value3>;
```

**将某一行的某一列的值设置为空**
```sql
UPDATE <tableName>
SET <column> = NULL
WHERE <column2> = <value2>;
```

**将整列设置为某个值**
```sql
UPDATE <tableName>
SET <columnName> = <value>;
```

**删除表中的某行**
```sql
DELETE FROM <tableName>
WHERE <columnName> = <value>;
```

**删除表中所有数据（慎用）**
```sql
DELETE FROM <tableName>;
```

## 6.自动保存、保存与回滚

在MySQL中，默认开启自动保存。也就是说你每次做的任何更改都会自动保存。  

**关闭或开启自动保存**
```sql
-- 关闭自动保存
SET AUTOCOMMIT = OFF;
-- 开启自动保存
SET AUTOCOMMIT = ON;
```

**手动保存**
```sql
COMMIT;
```

**回滚**  
在自动保存关闭的状态下，如果出现错误更改，我们可以归滚到上一次保存。  
```sql
ROLLBACK;
```

## sql中的保留符号

|名称|符号|
|---|---|
|空|`NULL`|

## sql中的比较操作符

|名称|符号|
|---|---|
|等于|`=`|
|大于|`>`|
|小于|`<`|
|不等于|`!=`|


## 其他注意事项

1. sql中判断是否是空只能用`IS`