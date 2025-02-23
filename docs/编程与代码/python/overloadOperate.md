# 重载运算符

在 Python 中，可以通过定义特殊方法（也称为魔术方法）来重载运算符，使得自定义的类可以使用 `+`、`-`、`*`、`/` 等运算符。这些特殊方法通常以双下划线（`__`）开头和结尾，例如 `__add__`、`__sub__`、`__mul__` 和 `__truediv__`。

---

## 1. **基本运算符重载**
Python 允许你为自定义类重载以下运算符：
| 运算符 | 方法 |
|--------|--------|
| `+` | `__add__(self, other)` |
| `-` | `__sub__(self, other)` |
| `*` | `__mul__(self, other)` |
| `/` | `__truediv__(self, other)` |
| `//` | `__floordiv__(self, other)` |
| `%` | `__mod__(self, other)` |
| `**` | `__pow__(self, other)` |

---

## 2. **示例**
假设我们有一个表示二维向量的 `Vector2D` 类，我们可以重载 `+`、`-`、`*` 和 `/` 运算符：

```python
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """重载 + 运算符"""
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        raise TypeError("Unsupported type for addition")

    def __sub__(self, other):
        """重载 - 运算符"""
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        raise TypeError("Unsupported type for subtraction")

    def __mul__(self, scalar):
        """重载 * 运算符（数乘）"""
        if isinstance(scalar, (int, float)):
            return Vector2D(self.x * scalar, self.y * scalar)
        raise TypeError("Multiplication only supports scalars")

    def __truediv__(self, scalar):
        """重载 / 运算符（数除）"""
        if isinstance(scalar, (int, float)):
            if scalar == 0:
                raise ZeroDivisionError("Division by zero")
            return Vector2D(self.x / scalar, self.y / scalar)
        raise TypeError("Division only supports scalars")

    def __repr__(self):
        """定义对象的字符串表示"""
        return f"Vector2D({self.x}, {self.y})"

# 测试
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

print(v1 + v2)   # Vector2D(4, 6)
print(v1 - v2)   # Vector2D(2, 2)
print(v1 * 2)    # Vector2D(6, 8)
print(v1 / 2)    # Vector2D(1.5, 2.0)
```

---

## 3. **支持反向运算**
Python 允许通过 `__radd__`、`__rsub__`、`__rmul__` 等方法支持 **反向运算**（即 `右侧操作数` 参与计算）。例如：

```python
class Vector2D:
    # (省略 __init__ 方法)

    def __mul__(self, scalar):
        """支持左乘"""
        if isinstance(scalar, (int, float)):
            return Vector2D(self.x * scalar, self.y * scalar)
        raise TypeError("Multiplication only supports scalars")

    def __rmul__(self, scalar):
        """支持右乘"""
        return self.__mul__(scalar)

# 测试
v = Vector2D(1, 2)
print(2 * v)   # Vector2D(2, 4)  （反向运算）
```

---

## 4. **支持 in-place 赋值运算符（+=、-=、*=、/=）**
Python 还提供了 `__iadd__`、`__isub__`、`__imul__`、`__itruediv__` 等方法，使对象能够支持 `+=`、`-=` 等原地运算。例如：

```python
class Vector2D:
    # (省略 __init__ 方法)

    def __iadd__(self, other):
        """支持 += 运算符"""
        if isinstance(other, Vector2D):
            self.x += other.x
            self.y += other.y
            return self  # 直接修改当前对象
        raise TypeError("Unsupported type for addition")

    def __isub__(self, other):
        """支持 -= 运算符"""
        if isinstance(other, Vector2D):
            self.x -= other.x
            self.y -= other.y
            return self
        raise TypeError("Unsupported type for subtraction")

# 测试
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

v1 += v2
print(v1)  # Vector2D(4, 6)
```

---

## 5. **支持比较运算符**
可以重载 `__eq__`、`__ne__`、`__lt__`、`__le__`、`__gt__`、`__ge__` 来支持比较运算：

```python
class Vector2D:
    # (省略 __init__ 方法)

    def __eq__(self, other):
        """重载 == 运算符"""
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return False

# 测试
v1 = Vector2D(3, 4)
v2 = Vector2D(3, 4)
v3 = Vector2D(1, 2)

print(v1 == v2)  # True
print(v1 == v3)  # False
```

---

## 6. **总结**
在 Python 中，可以通过重载运算符使自定义类支持各种操作。常见方法包括：
- `__add__`、`__sub__`、`__mul__`、`__truediv__` 处理 `+`、`-`、`*`、`/`。
- `__radd__`、`__rmul__` 支持反向运算，如 `2 * v`。
- `__iadd__`、`__isub__` 处理 `+=`、`-=` 等原地运算。
- `__eq__`、`__ne__`、`__lt__`、`__le__` 处理比较运算。

通过运算符重载，可以让 Python 类更直观、更易用。