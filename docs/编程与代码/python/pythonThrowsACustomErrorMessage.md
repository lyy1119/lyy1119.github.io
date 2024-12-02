# Python抛出自定义的错误信息

![Static Badge](https://img.shields.io/badge/ALL_Generated_By-OpenAI-red)  


在Python中，可以通过继承内置的`Exception`类来创建自定义错误。自定义错误的作用是让代码更加清晰和易于调试，特别是在需要特定异常类型的情况下。

### 创建自定义错误的步骤

1. **继承 `Exception` 类**：创建一个新的类，继承Python的内置 `Exception` 类。
2. **添加自定义的初始化方法（可选）**：如果需要传递额外信息，可以重写 `__init__` 方法。
3. **抛出错误**：使用 `raise` 关键字抛出该错误。

### 示例代码

```python
# 定义自定义错误类
class CustomError(Exception):
    def __init__(self, message, code=None):
        super().__init__(message)  # 调用父类的构造函数
        self.code = code  # 添加自定义属性

# 使用自定义错误
try:
    user_input = int(input("请输入一个正数："))
    if user_input <= 0:
        raise CustomError("输入的不是正数！", code=400)
except CustomError as e:
    print(f"捕获到自定义错误: {e}")
    if hasattr(e, 'code'):
        print(f"错误代码: {e.code}")
```

### 输出示例
当用户输入 `-5` 时：
```
请输入一个正数：-5
捕获到自定义错误: 输入的不是正数！
错误代码: 400
```

### 应用场景
- 自定义错误可以用于标识特定的逻辑错误（如业务逻辑或输入验证）。
- 结合代码调试日志，用于跟踪更详细的错误信息。