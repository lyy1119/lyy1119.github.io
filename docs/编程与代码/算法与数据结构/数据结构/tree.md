# 树

## 定义

[维基百科_树](https://zh.wikipedia.org/wiki/%E6%A0%91_(%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84))

## 二叉树 Binary tree

只有左右两分支的树。  

### 二叉树的顺序存储

将二叉树从根节点到叶，一次从左到右存入顺序存入列表，如下图所示。  

![20250126153344](https://raw.githubusercontent.com/lyy1119/Imgs/main/img/20250126153344.png)  

则父节点和子节点索引的关系为：若父节点索引为\( i \) ，则子左节点为 \( 2i+1 \) ，子右节点为 \( 2i+2 \) 。若子节点索引为 \( i \) ，则父节点的所有为 \( (i-1)//2 \) （整除）。  

### 二叉树的遍历顺序

1. 前序遍历
2. 中序遍历
3. 后序遍历
4. 层级遍历

![20250202145758](https://raw.githubusercontent.com/lyy1119/Imgs/main/img/20250202145758.png)

**代码实现** ：  
```python
# python
# 前序遍历
def pre_order(root):
    if root:
        print(root)
        pre_order(root.leftChild)
        pre_order(root.rightChild)
# 中序遍历
def in_order(root):
    if root:
        pre_order(root.leftChild)
        print(root)
        pre_order(root.rightChild)
# 后序遍历
def post_order(root):
if root:
        pre_order(root.leftChild)
        pre_order(root.rightChild)
        print(root)
# 层次遍历
# 使用队列实现
from collections import deque
def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        node = queue.popleft()
        print(node.data)
        if node.leftChild:
            queue.append(node.leftChild)
        if node.rightChild:
            queue.append(node.rightChild)
```
