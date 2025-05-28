# 更快的标准输入输出（stdio）

## 更快的输入

当数据量比较大的时候，使用`input()`处理输入会比较慢，可以使用`sys.stdin.readline()`，这样输入会更快些。  

```python title="sys.stdin.readline"
import sys

def input(): # overwrite input
    return sys.stdin.readline()
```

## 更快的输出

使用`sys.stdout.write()`可以获得更快的输出，但是不会刷新缓冲区。  

```python title="sys.stdout.write()"
sys.stdout.write("output something, but can not print \\n automatically.")
```