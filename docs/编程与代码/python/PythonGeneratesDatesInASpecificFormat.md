# Python生成指定格式的日期

![Static Badge](https://img.shields.io/badge/ALL_Generated_By-OpenAI-red)  

在Python中，可以使用`datetime`模块来生成和格式化日期。要以`yyyy-mm-dd`的格式生成当前日期，可以使用如下代码：

```python
from datetime import datetime

# 获取当前日期并格式化为 'yyyy-mm-dd'
current_date = datetime.now().strftime('%Y-%m-%d')
print(current_date)
```

这段代码会输出当前日期，格式为 `yyyy-mm-dd`，例如 `2024-12-01`。