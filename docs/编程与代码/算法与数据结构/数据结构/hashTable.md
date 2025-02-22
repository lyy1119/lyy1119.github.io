# 哈希表 Hash Table

又称 **散列表** 。  

以下是[维基百科](https://zh.wikipedia.org/wiki/%E5%93%88%E5%B8%8C%E8%A1%A8)中对哈希表的解释。  
> 散列表（英语：Hash table）是根据键而直接访问在存储器存储位置的数据结构。也就是说，它通过计算出一个键值的函数，将所需查询的数据映射到表中一个位置来让人访问，这加快了查找速度。这个映射函数称做散列函数，存放记录的数组称做散列表。  

*Python的字典和集合就是使用哈希表实现的。*  

哈希表一般支持以下这三个操作：
- 插入键值对： **insert**
- 有键获取值： **get(key)**
- 根据键删除值： **delete(key)**

## 哈希表的特例——直接寻址表

直接寻址表是一种最简单的键值存储方式，适用于 **键值范围固定且较小** 的情况。  

直接寻址表可以看作是一种**特殊的哈希表**，其中**哈希函数为恒等函数**（即 \( h(k) = k \)），并且键的范围正好适配数组大小。

### 工作原理
- 设键的取值范围为 \([0, U-1]\)，即所有可能的键都在一个固定范围内。
- 直接创建一个大小为 \( U \) 的数组 `T[0:U-1]`，其中：
  - 若某个键 \( k \) 存在，则 `T[k]` 处存储对应的值。
  - 若 \( k \) 不存在，则 `T[k]` 为空（可以是 `None` 或特殊标记）。
- 插入、删除、查找的时间复杂度均为 \( O(1) \)。

### 优缺点
✅ **优点**：
- 查找速度极快，所有操作均为 \( O(1) \)。
- 结构简单，容易实现。

❌ **缺点**：
- 当键的范围 \( U \) 很大时，会造成**空间浪费**，因为即使只使用了很少的键，整个数组仍然需要占用 \( O(U) \) 的空间。
- 仅适用于**键的范围较小且稠密的情况**，否则会导致大量未使用的数组元素。


## 哈希的概念

哈希就是一个映射函数，将键通过一个函数映射到另一个域。  

**取余** 操作就是一种哈希。  

## 哈希冲突

**哈希冲突** 是指 **不同的键经过哈希函数计算后映射到相同的哈希表索引** ，导致多个数据试图存放在相同的位置。由于哈希表的大小通常远小于可能的键值范围，冲突是 **不可避免** 的，需要特殊的处理方法来解决。

---

### 为什么会发生哈希冲突？
假设我们有一个哈希表，大小为 `m = 10`，而存储的键可能有数百个甚至更多。如果使用哈希函数：
\[
h(k) = k \mod 10
\]
那么，所有与 `10` 同余的键（如 `10, 20, 30...`）都会映射到同一个索引，导致冲突。例如：
```python
h(10) = 10 % 10 = 0
h(20) = 20 % 10 = 0
h(30) = 30 % 10 = 0
```
这就造成了哈希冲突，因为 `10, 20, 30` 都映射到了索引 `0`。

---

### 解决哈希冲突的方法
为了有效使用哈希表，我们需要 **冲突解决策略** ，主要有以下几种：
- 链地址法
- 线性探测
- 二次探测
- 双重哈希