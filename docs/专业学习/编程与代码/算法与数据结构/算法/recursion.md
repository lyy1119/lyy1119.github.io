# 递归

## 递归的两个特点

1. 调用自身
2. 结束条件（边界条件）

## 典型问题——汉诺塔

### 问题描述

略

### 解答

```python
def hanoi(n , a , b , c):
    '''
    move n plate from a to c by b
    '''
    if n > 0:
        hanoi(n-1 , a , c , b)
        print(f"move {a} to {c}")
        hanoi(n-1 , b , a , c)
    else:
        pass

if __name__ == "__main__":
    hanoi(6 , "a" , "b" , "c")
```