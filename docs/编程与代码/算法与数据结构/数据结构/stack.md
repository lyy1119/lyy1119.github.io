# 栈 Stack

先进后出、后进先出的数据结构，类似手枪弹匣。  

**栈的特点** ：后进先出。  
**栈的相关概念** ： **栈顶** 、 **栈底** 。  
**栈的基本操作** ：
- 进栈（压栈）push
- 出栈 pop
- 取栈顶 gettop

![20250130174253](https://raw.githubusercontent.com/lyy1119/Imgs/main/img/20250130174253.png)  

**python中栈的简单实现** ：  
- 进栈：`list.append(i)`
- 出栈：`list.pop()`
- 取栈顶：`list[-1]`

```python
# python
class Stack:
    def __init__(self):
        self.data = []

    def push(self , element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def get_top(self):
        if len(self.data) > 0:
            return self.data[-1]
        else:
            return None
```

## 栈的应用

**括号匹配问题** ：判断一堆字符中的括号是否相匹配。  