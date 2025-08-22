# 3.矩阵

所谓矩阵就是多个数组成的阵列。这里主要讨论二维矩阵，也就是由 $n$ 行 $m$ 列组成的数字阵列，如下是一个两行三列的矩阵：  

$$
\mathbf{A} = \left(
    \begin{matrix}
        1 & 2 & 3 \\
        4 & 5 & 6
    \end{matrix}
\right)
$$

## 关于矩阵

**矩阵的本质** ： 线性变换  

**矩阵的运算** ： 加法、数乘、矩阵相乘  

1.**矩阵的加法**：加法的前提是两矩阵行列各相等，矩阵的加法运算即对应行列上的数字相加。如：  

$$
\left(
    \begin{matrix}
        1 & 2 & 3 \\
        4 & 5 & 6
    \end{matrix}
\right) + \left(
    \begin{matrix}
    1 & 0 & 1 \\
    0 & 1 & 0
    \end{matrix}
\right) = \left(
    \begin{matrix}
        2 & 2 & 4 \\
        4 & 6 & 6
    \end{matrix}
\right)
$$

2.**矩阵的数乘**：所谓数乘，即一个数乘以一个矩阵。运算时将矩阵所有元素都乘以相同的数，如：  

$$
2 \times \left(
    \begin{matrix}
        1 & 0 \\
        0 & 1
    \end{matrix}
\right) = \left(
    \begin{matrix}
    2 & 0 \\
    0 & 2
    \end{matrix}
\right)
$$

3.**矩阵相乘**：即两个矩阵的乘法。矩阵相乘在线性代数中是一个重要的运算，定义大致如下：  
> 若有两个矩阵，分别记为 $\mathbf{A}$ 和 $\mathbf{B}$ ，若矩阵 $\mathbf{A}$ 有 $n$ 行 $m$ 列，矩阵 $\mathbf{B}$ 有 $m$ 行 $n$ 列，则两矩阵可相乘，**且仅能** 以 $\mathbf{AB}$ 形式相乘，即 $\mathbf{A}$ 左乘 $\mathbf{B}$。  
>
> 记运算结果为 $\mathbf{C}$ ，即 $\mathbf{AB} = \mathbf{C}$ 。 矩阵 $\mathbf{C}$ 的各元素结果如下：  
> 若记矩阵 $\mathbf{A}$ $\mathbf{B}$ $\mathbf{C}$ 的第 $i$ 行 $j$ 列元素分别为 $a_{ij}$ $b_{ij}$ $c_{ij}$ ，则 $c_{ij} = \sum^{m}_{p=1}{a_{ip} b_{pj}} $

例：  

$$
\left(
    \begin{matrix}
        1 & 2 & 3 \\
        4 & 5 & 6
    \end{matrix}
\right)\left(
    \begin{matrix}
        1 & 0 \\
        0 & 1 \\
        1 & 0
    \end{matrix}
\right) = \left(
    \begin{matrix}
        4 & 2 \\
        10 & 5
    \end{matrix}
\right)
$$

4.**矩阵的转置**：矩阵转置的定义为矩阵元素的行列位置互换，记 原来的 $a_{ij}$ 在矩阵转置后变成 $a_{ji}$ 。在矩阵右上角写一个 $\text{T}$ 来表示转置操作  

$$
\left(
    \begin{matrix}
    1 & 2 & 3
    \end{matrix}
\right)^T = \left(
    \begin{matrix}
    1 \\
    2 \\
    3
    \end{matrix}
\right)
$$