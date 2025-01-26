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

## 1.冒泡排序 bubble sort

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

## 2.选择排序 selection sort

循环遍历 \( n \) 次列表（ \( n \) 为列表规模）。每次寻找无序区的最小值（升序排序），并按照顺序依次与第 \( i \) 个交换（ \( i \) 表示第几大的数），并缩小无序区。  

### 代码实现

```python
# python
def sort(li: list):
    for i in range(len(li) - 1):
        minValue = min(li[i:])
        minIndex = li.index(minValue , i)
        li[i] , li[minIndex] = li[minIndex] , li[i]
```

## 3.插入排序 insertion sort

排列元素时如同摸扑克牌一样，将有序区不断扩大，将“新摸到的牌”按元素顺序插入到有序区中。需要比较新元素和有序区元素大小，并实现插入操作。

### 代码实现

```python
# python
def insertion_sort(li: list):
    # 升序排序
    length = len(li)
    for i in range(1 , length):
        # print(li , i)
        # i 代表有序区右侧索引
        # 比较
        temp = li[i]    # 保存要插入的值
        for j in range(i - 1 , -2 , -1):
            # 反向遍历
            # print(j)
            if li[j] > temp and j != -1:
                # 如果索引为j的元素比索引为i的元素大，则索引为i的元素应该插入在索引为j的元素前，索引为j的元素后移
                li[j+1] = li[j]
            else:
                # 索引为j的元素小于等于索引为i的元素，插入元素应当插入在j+1，不移动元素，将值插入到j+1
                li[j+1] = temp
                break
```

## 4.快速排序

类似二分的理念，从无序列表中随机寻找一个元素（一般选取第一个），通过 **Partition** 操作，将元素放置在其 **正确位置** 然后对左右两个无序子列表做相似的分割操作。  

快速排序的时间复杂度是 \( O(n \log n) \) 。  

### Partition

使用两个元素记录目标列表的左右端元素索引，将用于Partition操作的元素记为“中间元素”，在升序排序时，依次移动右/左索引标记，将右侧小于中间元素的元素放置在左侧，这样右侧就有一个空位；然后将右侧小于中间元素的数放在左侧，循环往复，直到左侧索引大于右侧。  

### 代码实现——递归

```python
# python
def partition(li: list , left: int , right: int):
    pickOut = li[left]
    while left < right:
        while left < right and li[right] > pickOut:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] < pickOut:
            left += 1
        li[right] = li[left]
    # 左右交换完成，left=right=捡出元素的正确位置
    li[left] = pickOut
    return left

def quick_sort(li: list , left: int , right: int):
    if left < right:
        mid = partition(li , left , right)
        quick_sort(li , left , mid - 1)
        quick_sort(li , mid + 1 , right)
```

**问题** ：  
1. 使用了递归，消耗资源
2. 若每次partition的操作元素都是最大或者最小的，则每次递归列表无序长度只会减一，会出现所谓 **最坏情况** 。（解决方法：将partition选取的元素随机化）  

## 5.堆排序