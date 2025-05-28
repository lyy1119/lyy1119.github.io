# E - Most Valuable Parentheses

[原题连接](https://atcoder.jp/contests/abc407/editorial/13107)  

## 解题思路

对于一个合法的括号序列，具有以下特征：  
- 长度为`2N`的序列，必然有`N`个`(`和`)`
- 对于前`i`个序列，至少有 $\frac{i}{2}$ 个`(`
- 第一个必然是`(`且最后一个必然是`)`

对于该题，我们要做的是在合法的情况下，将`(`安排在最大的数上。  

对于第一个数，必然是`(`，对于接下来的数，已知每`2i`个（ $1 \leq i \leq N$ ）个数中至少有`i`个`(`。同时，不难得出，对于`1~2i-1`，也至少有`i`个`(`。  

这题可以使用大根堆解决，除第一个是固定的`(`外，可以每两个入一次堆，然后取堆顶，即当前数中最大的，当`i=0`时，入堆`i*2-0`；当`i>1`时，入堆`i*2-0`及`i*2-1`，这样便可以实现每个子序列都满足合法序列条件，即是一个合法的括号序列。  

## Python代码
```python title="E - Most Valuable Parenthese"
import heapq

for _ in range(int(input())):
    n = int(input())
    numbers = [int(input()) for _ in range(2*n)]
    answer = 0
    h = []
    heapq.heapify(h)
    for i in range(n):
        if i == 0:
            heapq.heappush(h,-numbers[0])
        else:
            heapq.heappush(h, -numbers[i*2 - 1])
            heapq.heappush(h, -numbers[i*2 - 0])

        answer += -heapq.heappop(h)
    print(answer)
```
