# 从N个数中选取K个数

现在给你以下参数： \( n \) 、 \( k \) 和一个长度为 \( n \) 数字列表，让你从中选取k个数（无顺序，且 \( n < k \) ）。

## 思路

显然，k是未知的，不能直接用for循环求解。可以考虑使用递归求解。  

对于这样一个问题，递归的中止条件是待选列表只剩下一个数。那么可以这样考虑：  

函数的功能是从一个列表的指定区域（候选区）选取 \( n \) 个数，其子任务是从一个更小的候选区选取 \( n-1 \) 个数。而对于选取的第一个数有如下选取可能：即从候选区第一个到倒数第n个。  

## 代码实现

```python
def selectNumber(start: int , stop: int , k: int , li: list) -> list:
    res = []
    if k > 0:
        for i in range(start , stop + 2 - k):
            r = selectNumber(i+1 , stop , k-1 , li)
            if r:
                for j in r:
                    a = [li[i]]
                    a.extend(j)
                    res.append(a)
            else:
                res.append([li[i]])
    return res
```

## 进阶问题——有序数的排列组合

若给定从1到n这n个自然数，要求输出所有可能的排列组合，并按照字典顺序排序。

可以使用 **广度优先算法** ，先初始化一个可以作为头数字的、以列表为元素的列表。使用队列这一数据结构，将元素逐一出队，然后加上尾元素，再逐一入队，直至头元素的长度符合要求。

### 代码实现

```python
n = int(input()) # n表示给定的自然数范围，从1到n

from collections import deque

numbers = [i for i in range(1,n+1)]
res = deque([[i] for i in range(1,n+1)])

while len(res[0]) < n:
    i = res.popleft()
    for j in numbers:
        if j in i:
            continue
        else:
            newList = i.copy()
            newList.append(j)
            res.append(newList)
```