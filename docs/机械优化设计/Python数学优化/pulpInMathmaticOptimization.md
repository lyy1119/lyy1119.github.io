# python使用pulp求解优化模型

## pulp库的安装

```shell
pip install pulp
```

## 快速示例

python实例代码：  

```python
import pulp

model = pulp.LpProblem('1', pulp.LpMinimize) # 创建问题对象
# 创建设计参数 ， 其中 cat=pulp.LpInteger 表示设计参数为整数
# lowBound=0用于设置变量的下边界，与约束条件作用相同
x1 = pulp.LpVariable("x1", lowBound=0 , cat=pulp.LpInteger)
x2 = pulp.LpVariable("x2", lowBound=0 , cat=pulp.LpInteger)

# 添加目标函数，可以用逗号隔开给上注释
model += 40*x1 + 36*x2, "cost"
# 添加约束条件
model += 8*25*x1 + 8*15*x2 >= 1800
model += x1 - 8 <= 0
model += x2 - 10 <= 0
# 求解模型
model.solve()
# 输出结果
print("状态:", pulp.LpStatus[model.status])
print("最优值:", pulp.value(model.objective))
print("x =", x1.value(), "x2 =", x2.value())
```

## 具体用法

### 1.创建问题对象

### 2.添加目标函数和约束条件

### 3.求解问题和输出结果