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