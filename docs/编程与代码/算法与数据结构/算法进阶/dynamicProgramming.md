# 动态规划 Dynamic Programming

动态规划，简称 **DP** 。  

动态规划不是某一种算法，而是一种思想。  

## 动态规划的中心思想

- 递推式
- 重复的子问题

## 从斐波那契数列理解动态规划

[斐波那契数列 Wikipedia](https://zh.wikipedia.org/wiki/%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0)  

求斐波那契数列中第n项的值可以有以下两种python实现：  
```python
def fibonacci_recursion(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

def fibonacci_no_recursion(n):
    fibonacci = [0 , 1 , 1]
    if n > 2:
        while len(fibonacci) <= n:
            length_fibonacci = len(fibonacci)
            fibonacci.append(fibonacci[length_fibonacci - 1] + fibonacci[length_fibonacci - 2])
    return fibonacci[n]
```

其中，递归的实现在n很大时，由于重复的子任务执行次数太多，其效率十分低下。而非递归的实现则避免了这一点。非递归的实现就可以看作是一种动态规划思想。  