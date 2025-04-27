# MySQL笔记

| [参考视频课程（YouTube）](https://www.youtube.com/watch?v=5OdVJbNCSso) |

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

!!! warning
    只要没有插入完整的各列数据，都需要指定插入的数据是哪几列的。

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

## 7.获取日期、时间、日期及时间

MySQL中有内置函数获取这些数据。  

我们可以创建如下表来测试。  

```sql
CREATE TABLE test(
	myDate DATE,
    myTime TIME,
    date_time DATETIME
);
-- 插入
INSERT INTO test
VALUES (
	CURRENT_DATE(), CURRENT_TIME(), NOW()
);
SELECT * FROM test;
```

其中可以对`CURRENT_DATE()`加1或者减1以获取明天或者昨天的日期。

## 8.表列数据限制

在Mysql中，可以对表的数据做一些限制，如某列下的数据不能相同，如uid。或者必须有值

**UNIQUE限制**  

!!! info
    `UNIQUE`其实是`UNIQUE KEY`的简写

`UNIQUE`限制保证这一列下的数据不能相同，添加限制有两种方法。一是在创建表时限制
```sql
CREATE TABLE products(
    productId   INT UNIQUE,
    productName VARCHAR(25),
    price       DECIMAL(10, 2)
);
```
以上语句给id列添加了限制条件：唯一。添加了这样的限制的列在加入一个具有相同值的数据时会报错。  

如果已经创建了表，可以通过以下语句添加限制条件。
```sql
ALTER TABLE products
ADD CONSTRAINT
UNIQUE(productName);
```

**NOT NULL限制**  
`NOT NULL`可以限制某列数据必须不为空，当尝试插入数据时，若该列为空，则会报错。  
```sql
-- 在创建时加限制
CREATE TABLE <tableName>(
    column1 <dataType> NOT NULL,
    column2 <dataType>
);
-- 对现有表加限制
ALTER TABLE <tableName>
MODIFY COLUMN <columnName> <dataType> NOT NULL;
```

**自定义限制CHEKC**  
除了上述限制，我们还可以自定义限制，如限制某一列的数据必须是大于或在某个区间内的数。这样的限制可以使用`CKECK`实现。  
```sql
-- 在创建表时添加限制
CREATE TABLE <tableName>(
    column1 <dataType>,
    column2 <dataType>,
    ...
    columnN <dataType>,
    CHECK (column1 >= 50)
);
```

建议给限制条件命名，这样方便改动表格时删除限制条件。  
```sql
-- 在创建表时添加限制
CREATE TABLE <tableName>(
    column1 <dataType>,
    column2 <dataType>,
    ...
    columnN <dataType>,
    CONSTRAINT <nameOfCheck> CHECK (column1 >= 50)
);
```

对已经创建的表，可以通过如下命令添加限制条件。  
```sql
ALTER TABLE <tableName>
ADD CONSTRAINT <nameOfCheck> CHECK (<condition>);
```

删除表中的某个限制条件  
```sql
ALTER TABLE <tableName>
DROP CHECK <nameOfCheck>;
```

## 9.列的默认值

对于有些写入操作，比如我们想在写入时自动记录时间，可以使用`DEFAULT`实现。  

在创建表时添加`DEFALUT`  
```sql
CREATE TABLE <tabName>(
    column1 <dataType> DEFAULT <value you wannt be default>,
    ...
);
```

对现有表加`DEFAULT`  
```sql
ALTER TABLE <tabName>
ALTER <colName> SET DEFAULT <value>;
```

!!! warning 
    使用`DEFAULT`属性后，插入值时若不想手动指定值，即让表使用设置的默认值，需要指定插入数据属于哪几行，也就是使用指定行的插入方式。

## 10.主键

**主键** 也是约束的一种，主键等同于 **NOT NULL** 加 **UNIQUE** ，但是一张表只能有一个主键。

创建表时指定主键  
```sql
CREATE TABLE <tabName>(
    column1 <dataType> PRIMARY KEY,
    column2 <dataType>,
    ...
    columnN <dataType>
);
```

对现有表加主键  
```sql
ALTER TABLE <tabName>
ADD CONSTRAINT
PRIMARY KEY(<columnName>);
```

## 11.功能与属性

**自增（AUTO_INCREMENT）**  

仅能对被设置成**KEY**的列设置自增属性，且一个表只能有一个有自增属性的列，被设置为自增属性的列在插入时若不指定值，则会从表的最后个值开始自增。  

若表为空，则默认从1开始。但可以手动修改开始的值。  

同时也可以在插入时指定值。  

**在创建表时设置自增属性**
```sql
CREATE TABLE <tabName> (
    -- 一般将主键作为自增的，数据类型只能为INT或BIGINT，如uid
    column1 <dataType> PRIMARY KEY AUTO_INCREMENT,
    ...
    column <dataType>
);
```

**对现有表加自增属性**
```sql
ALTER TABLE <tabName>
MODIFY COLUMN <colName> INT AUTO_INCREMENT;
```

**更改自增的下一个值**
```sql
ALTER TABLE <tabName>
AUTO_INCREMENT = <value>;
```

!!! warning
    如果设置的值比表最后一行的值小，下一个自增值会是表最后一行的下一个值。

## 12.索引/键

MySQL中的`KEY`其实就是索引。  

MySQL中有以下类型的键。  

| 类型 | 关键字 | 特点 |
|--|--|--|
| 主键 | PRIMARY KEY | 唯一且非空，表里只能有一个 |
| 唯一键 | UNIQUE KEY | 唯一，可以有多个 |
| 普通键（一般索引） | KEY / INDEX | 不要求唯一，主要加速查询 |

**在创建表时添加KEY**
```sql
CREATE TABLE <tabName> (
    column1 <dataType>,
    ...
    columnN <dataType>,
    KEY(<columnName>)
);
```

**对现有表加KEY**
```sql
ALTER TABLE <tabName>
ADD KEY (<columnName>);
-- 也可以给索引起名
ALTER TABLE <tabName>
ADD KEY <indexName> (<columnName>);
```
!!! warning
    索引名是给数据库优化内部执行速度用的，所有增减删改操作都应该使用列名。

## ADD CONSTRAINT的相关说明

添加constraint的语句书写完整形式如下  
```sql
ALTER TABLE <tabName>
ADD CONSTRAINT <constaintName>
<constrainType> (<columnName>);
```
其中`ADD CONSTRAINT <constaintName>`这一行可以全部省略，也可以只不写命名

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