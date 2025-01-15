# 排序（sort）

排序是将无序列表排序成有序列表的操作。排序有升序 **ascending order** 和降序 **descending order** 之分。  

## 常见排序算法

1. 冒泡排序 **Bubble sort**
2. 选择排序  **Selection sort**
3. 插入排序 **Insertion sort**
4. 快速排序 **Quick sort**
5. 堆排序
6. 归并排序
7. 希尔排序
8. 计数排序
9. 基数排序

## 1.冒泡排序

比较列表中两个相邻数，如果前面比后面大（升序排序），则交换两个数。  
冒泡排序每运行一个循环，列表有序区大小变大一个，无序区大小减小一个。每次只对无序区排序。初始时，整个列表都是无序区。  

因为当无序区只剩一个时，不用再排序，所以整个冒泡排序需要运行 \( n-1 \) 次循环。时间复杂度为 \( O(n^2) \) 。  

冒泡排序的关键： **循环次数** 、 **无序区范围** 。  

### 代码实现

```python
# python
def bubble_sort(li: list):
    # ascending order
    loopTimes = len(li) - 1
    for i in range(loopTimes):
        for j in range(0 , loopTimes - i):
            if li[j] > li[j+1]:
                li[j] , li[j+1] = li[j+1] , li[j]
```

### 改进

若某次循环中，没有发生交换，则说明排序已经完成。可以使用一个变量作为标志位来改进算法。  

实现如下：  
```python
# python
def bubble_sort(li: list):
    # ascending order
    loopTimes = len(li) - 1
    for i in range(loopTimes):
        exchange = False
        for j in range(0 , loopTimes - i):
            if li[j] > li[j+1]:
                exchange = True
                li[j] , li[j+1] = li[j+1] , li[j]
        if not exchange:
            break
```

