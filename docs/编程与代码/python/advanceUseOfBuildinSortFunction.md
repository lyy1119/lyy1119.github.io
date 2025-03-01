# python列表内置排序方法的使用

## 是否修改原数据

若要修改原数据，使用`list.sort()`  
```python
li = list()
li.sort()
```

若不需要修改原数据，使用`sorted()`方法  
```python
li = list()
sortedList = sorted(li)
```

## 是否逆序

列表的类方法和`sorted()`函数都有reverse参数，传入参数`revsere=True`即逆序排序。  
```python
li = list(range(10))
sorted(li , reverse=True)
li.sort(reverse=True)
```

## 自定义排序关键词

当列表元素为字典或者元素不是数字时，可以指定关键字的映射顺序来排序。同时，还可以指定多个关键字，按照先后顺序分为第一关键字、第二关键词……  
```python
li = [
    {
        "name" : "name1",
        "level" : 10
    },
    {
        "name" : "name2",
        "level" : 9
    },
]

# 按照level关键字排序
li.sort(key=lambda x: x["level"])

# 若有以下名字-数字映射
project = [
    "name1",
    "name2"
]

# 多关键字排序，先排level，level相同按照名字排序
li.sort(key=lambda x: (x["level"] , project.index(x["name"])))

# 默认是升序排序，在要排序的变量前加 - 号，可改为逆序
# sorted() 方法也有以上用法
```