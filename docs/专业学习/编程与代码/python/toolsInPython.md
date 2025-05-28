# Python内置算法工具

Python 的标准库中自带了很多非常好用的“算法工具”，尤其是在模块 `itertools`、`functools`、`heapq`、`collections`、`bisect` 等中。这些工具在算法题和工程开发中都非常常用。

## 🔁 `itertools` — **迭代器工具集合**

用于生成排列、组合、累积等：

| 工具 | 功能 |
|------|------|
| `permutations(iterable, r)` | r 长度的全排列，默认 r=len(iterable) |
| `combinations(iterable, r)` | r 长度的组合（不重复） |
| `product(iter1, iter2, ...)` | 笛卡尔积（类似嵌套循环） |
| `accumulate(iterable)` | 前缀和（默认），也可以自定义函数如乘积 |
| `groupby(iterable, key=...)` | 相邻相同元素分组（通常要先排序） |
| `cycle(iterable)` | 无限重复循环 iterable |
| `count(start=0, step=1)` | 无限整数生成器（类似 range） |
| `chain(iter1, iter2, ...)` | 把多个可迭代对象接成一个大迭代器 |

🧠 示例：
```python
from itertools import combinations, accumulate
print(list(combinations([1, 2, 3], 2)))  # [(1,2), (1,3), (2,3)]
print(list(accumulate([1, 2, 3, 4])))    # [1, 3, 6, 10]
```

---

## 🧠 `functools` — **函数式编程工具**

| 工具 | 功能 |
|------|------|
| `lru_cache` | 自动记忆函数结果，常用于递归优化 |
| `reduce(func, seq)` | 累积函数，比如求连乘 |
| `cmp_to_key(func)` | 比较函数转成排序 key |

🧠 示例：
```python
from functools import reduce, lru_cache
reduce(lambda x, y: x*y, [1, 2, 3, 4])  # 输出 24

@lru_cache
def fib(n): return n if n<=1 else fib(n-1)+fib(n-2)
```

## 🧺 `heapq` — **最小堆（优先队列）**

Python 默认是 **最小堆**（最小元素优先）

| 工具 | 功能 |
|------|------|
| `heapify(list)` | 把 list 变成堆 |
| `heappush(heap, item)` | 压入堆 |
| `heappop(heap)` | 弹出最小元素 |
| `heappushpop(heap, item)` | 先 push 再 pop，效率高 |

🧠 示例：  
```python
import heapq
h = [3, 1, 4]
heapq.heapify(h)
heapq.heappush(h, 2)
heapq.heappop(h)  # 弹出最小值 1
```


## 📚 `collections` — **高级数据结构集合**

| 工具 | 功能 |
|------|------|
| `deque` | 高效的双端队列（支持 `appendleft`, `pop`） |
| `Counter` | 计数器，自动统计元素频率 |
| `defaultdict` | 带默认值的字典，避免 KeyError |
| `OrderedDict` | 保留插入顺序的字典（Python 3.7+ 内置） |
| `namedtuple` | 给 tuple 加名字，像轻量类 |

🧠 示例：  
```python
from collections import Counter, defaultdict, deque
c = Counter('abracadabra')  # {'a':5, 'b':2, ...}
d = defaultdict(int)        # 默认值是0
q = deque([1,2,3])
q.appendleft(0)
```


## 📍 `bisect` — **二分查找工具**

处理 **有序数组** 的插入查找问题：

| 工具 | 功能 |
|------|------|
| `bisect_left(a, x)` | 找到 x 应插入的位置（靠左） |
| `bisect_right(a, x)` | 找到 x 应插入的位置（靠右） |
| `insort_left(a, x)` | 插入 x 并保持顺序（靠左） |
| `insort_right(a, x)` | 插入 x 并保持顺序（靠右） |

🧠 示例：
```python
import bisect
a = [1, 3, 5, 7]
bisect.bisect_left(a, 4)  # 输出 2
bisect.insort(a, 4)       # a 变为 [1, 3, 4, 5, 7]
```

## 常用算法组合：
- `heapq` + `dijkstra`
- `lru_cache` + 记忆化递归
- `itertools.product` + 枚举状态
- `bisect` + 前缀和
- `Counter` / `defaultdict` + 滑动窗口

