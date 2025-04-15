# 二叉搜索树

以下是来自[维基百科](https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9)的解释：  

二叉查找树，也称为二叉搜索树、有序二叉树（ordered binary tree）或排序二叉树（sorted binary tree），是指一棵空树或者具有下列性质的二叉树：  

- 若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；  
- 若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值；  
- 任意节点的左、右子树也分别为二叉查找树；  

二叉查找树相比于其他数据结构的优势在于查找、插入的时间复杂度较低。为 \( O(\log n) \)。二叉查找树是基础性数据结构，用于构建更为抽象的数据结构，如集合、多重集、关联数组等。  

## 二叉搜索数的实现

### 插入

从根节点开始，如果该节点的值比插入值大，向左子树继续；如果该节点的数比插入值小，向右子树继续。直至左子节点或右子节点为空。将值插入到目标左子节点或右子节点。  

### 查询

从根节点开始，当前节点比目标值大就向左子节点搜索，当前节点比目标值小就向右子节点搜索，直至搜索到或者当前节点指向`None`。  

### 删除

分为三种情况。  

#### 1.删除的节点是叶节点

这是最简单的情况，直接删除父节点与该节点的连接，然后删除该节点即可。  

#### 2.删除的节点右一个子节点

将父节点和子节点连接即可。要注意判断要删除的节点是父节点的左还是右节点，然后正确连接。  

#### 3.删除的节点有两个子节点

找到以当前节点为树的、刚好比当前节点的值大或者小的数，即找当前节点的左子树的最大值或者右子树的最小值。然后替换当前节点的值，并删除找到的那个节点。  

#### 特殊情况

当删除的节点是根节点是，需要注意根节点没有父节点。因此还需要做额外或更少的处理。并且需要更新根节点指针。


## 代码实现

以下是python的BinarySearchTree的一个实现。  

```python
# python

class BST:
    class Node:
        def __init__(self , value , lChild=None , rChild=None , parent=None):
            self.value = value
            self.lChild = lChild
            self.rChild = rChild
            self.parent = parent

    def __init__(self , head=None):
        self.head = head
    
    def insert(self , value) -> bool:
        # 如果是空树
        if self.head == None:
            # 直接创建新节点
            self.head = self.Node(value)
            return True
        else: # self.head != None
            currentNode = self.head
            while True:
                if currentNode.value == value:
                    return False # 不插入
                elif currentNode.value > value:
                    if currentNode.lChild == None:
                        # 插入
                        currentNode.lChild = self.Node(value)
                        currentNode.lChild.parent = currentNode
                        return True
                    else:
                    # 向左寻找
                        currentNode = currentNode.lChild
                elif currentNode.value < value:
                    if currentNode.rChild == None:
                        currentNode.rChild = self.Node(value)
                        currentNode.rChild.parent = currentNode
                        return True
                    else:
                        # 向右寻找
                        currentNode = currentNode.rChild

    @staticmethod
    def recursion_tree(Node) -> str:
        res = ''
        if Node:
            res += BST.recursion_tree(Node.lChild)
            res += str(Node.value)
            res += BST.recursion_tree(Node.rChild)
        return res
    
    def __str__(self):
        if self.head == None:
            return "None"
        return BST.recursion_tree(self.head)
    
    def delete(self , value) -> bool:
        # 寻找该值
        currentNode = self.head
        while currentNode:
            if value > currentNode.value:
                currentNode = currentNode.rChild
            elif value < currentNode.value:
                currentNode = currentNode.lChild
            elif value == currentNode.value:
                break
        else:
            return False
        # 判断：
        # 头节点
        if currentNode == self.head and currentNode.lChild == None and currentNode.rChild == None:
            # 如果头节点下面是空的
            self.head = None
            del currentNode
            return True
        # 叶节点
        elif currentNode.lChild == None and currentNode.rChild == None:
            # 直接删除
            if currentNode.parent.value > currentNode.value:
                # 是父节点的左子节点
                currentNode.parent.lChild = None
                del currentNode
                return True
            else: # 是父子节点的右节点
                currentNode.parent.rChild = None
                del currentNode
                return True
        # 有左右两子节点
        elif currentNode.rChild != None and currentNode.lChild != None:
            # 寻找左子树最大数代替当前，并删除最大数所在节点
            maxmumNode = currentNode.lChild
            while maxmumNode.rChild:
                maxmumNode = maxmumNode.rChild
            maxValue = maxmumNode.value # 存值
            if self.delete(maxmumNode.value): # 如果删除成功
                currentNode.value = maxValue
                return True
            else:
                return False
        # 仅有一个子节点
        elif currentNode.lChild != None or currentNode.rChild != None:
            if currentNode == self.head:
                # 如果要删除的是根节点：
                if currentNode.lChild:
                    self.head = currentNode.lChild
                    del currentNode
                    return True
                else:
                    self.head = currentNode.rChild
                    del currentNode
                    return True
            elif currentNode.lChild:
                # 如果左子节点存在：
                # 将左子节点和当前节点的父节点连接
                currentNode.lChild.parent = currentNode.parent
                if currentNode.parent.lChild == currentNode:
                    currentNode.parent.lChild = currentNode.lChild
                else:
                    currentNode.parent.rChild = currentNode.lChild
                del currentNode
                return True
            if currentNode.rChild:
                currentNode.rChild.parent = currentNode.parent
                if currentNode.parent.lChild == currentNode:
                    currentNode.parent.lChild = currentNode.rChild
                else:
                    currentNode.parent.rChild = currentNode.rChild
                del currentNode
                return True
```