# 队列 Queue

**队列的相关概念** ：  
- 队尾 rear
- 对头 front

**队列的性质** ：先进先出。  

## 队列的实现（python）

![20250131165359](https://raw.githubusercontent.com/lyy1119/Imgs/main/img/20250131165359.png)  

假定列表是环形的，用两个变量存 **front** 和 **rear** 的索引，其中front的索引是实际队头元素的 \( 索引-1 \) 。当rear和front变量所存索引相同时，表面 **队空** ，当front和rear所存索引数字为 \( front - 1 = rear \) 时，表示 **队满** ，每次出队或者入队，front和rear分别+1并对队列长度取模。  

## 基于python list的代码实现

```python
class Queue:
    def __init__(self , size = 100):
        self.front = 0
        self.rear = 0
        self.data = [0 for i in range(size + 1)]
        self.size = 100

    def push(self , element):
        self.rear = (self.rear + 1) % self.size
        self.data[self.rear] = element

    def pop(self):
        self.front = (self.front + 1) % self.size
        return self.data[self.front]

    def is_empty(self):
        return (self.front == self.rear)
    
    def is_filled(self):
        return (self.rear + 1) % self.size == self.front
```