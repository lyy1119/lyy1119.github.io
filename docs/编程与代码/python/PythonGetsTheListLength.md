# Python获取列表长度

![Static Badge](https://img.shields.io/badge/Generated_By-OpenAI-red)

在 Python 中，可以使用内置函数 `len()` 获取列表的长度。以下是一个简单的示例：

```python
# 定义一个列表
my_list = [1, 2, 3, 4, 5]

# 获取列表长度
length = len(my_list)

print(f"列表的长度是: {length}")
```

运行结果：
```
列表的长度是: 5
```

### 适用范围
`len()` 不仅适用于列表，还适用于其他数据结构，例如字符串、元组、字典、集合等。它的通用语法是：
```python
length = len(container)
```

例如：
- 字符串长度：`len("hello")` 返回 `5`
- 字典键值对数量：`len({"a": 1, "b": 2})` 返回 `2`
- 集合元素数量：`len({1, 2, 3})` 返回 `3`