# 链表 Linked list

与C/C++的链表概念相同。链表由一系列节点（ **Node** ）组成。每个节点包含两部分，数据和指向下一个节点的指针。  

![20250201174216](https://raw.githubusercontent.com/lyy1119/Imgs/main/img/20250201174216.png)  

## python中链表的实现

```python
# python
class Node:
    def __init__(self , item=None):
        self.item = item
        self.next = None
        pass

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = self.head
        pass

    def insert(self , element , pos=-1):
        if pos == -1:
            newNode = Node()
            newNode.item = element
            self.tail.next = newNode
            self.tail = newNode

    def print(self):
        nowNode = self.head.next
        while nowNode != None:
            print(nowNode.item)
            nowNode = nowNode.next
```