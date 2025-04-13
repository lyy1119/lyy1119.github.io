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