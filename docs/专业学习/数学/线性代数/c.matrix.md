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

5.**矩阵的行列式**：当矩阵为方阵时（即行数与列数相同），存在**矩阵的行列式**这一概念，即与矩阵元素相同的行列式。矩阵的行列式在几何中具有具体的意义，这将在矩阵的几何意义中讨论。  

矩阵行列式的记法： $\det{\mathbf{A}}$ 或 $|\mathbf{A}|$ 。  

矩阵行列式的运算性质：  
1. $|\mathbf{A}^\text{T}| = |\mathbf{A}|$
2. $|\lambda \mathbf{A}| = \lambda^n |\mathbf{A}|$ ( $n$ 为方阵行（列）数目)
3. $|\mathbf{AB}|=|\mathbf{A}|\cdot|\mathbf{B}|$

## 矩阵的几何意义

### 单位矩阵

在讨论几何意义之前，我们还需要知道一个概念——**单位（矩）阵**。  

**单位矩阵**：若矩阵 $\mathbf{A}$ 为单位矩阵，则对于其元素 $a_{ij}$ ，当 $i=j$ 时， $a_{ij} = 1$ ；反之， $a_{ij} = 0$ 。  

一般将单位阵记作 $\mathbf{E}$ 。下面就是一个3行3列的单位矩阵.  

$$ \mathbf{E} = \left(\begin{matrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & 1
\end{matrix}
    \right)$$

### 向量

**向量**可以看作是一种特别的矩阵。即只有一行或者一列的矩阵。  

我们将只有一行的矩阵称作 **行向量**；同理，将只有一列的矩阵称作 **列向量**。  

### 列向量与方阵的运算

当一个列向量与方阵运算时，对于一个比较特殊的情况——单位阵乘以列向量，其运算结果如下：  

$$ \left(
    \begin{matrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & 1
    \end{matrix}
\right)\left(\begin{matrix}
    x \\
    y \\
    z
\end{matrix}
\right) = \left(
    \begin{matrix}
        1\cdot x + 0 \cdot y + 0 \cdot z\\
        0\cdot x + 1 \cdot y + 0 \cdot z\\
        0\cdot x + 0 \cdot y + 1 \cdot z
    \end{matrix}
\right) = \left(
    \begin{matrix}
        x \\
        y \\
        z
    \end{matrix}
\right)
    $$

对于中间的表达式，如果以加号为分隔，竖向来看，每一列都是一个坐标（$x$或$y$或$z$）乘分别乘以三个数。  

让我们回想三维空间中坐标的三个数的意义——即这个点相对于原点在三个方向上的偏移量，或正或负。现在，矩阵左乘向量就有些眉目了——似乎是沿着某三个向量各偏移 $x$ 、 $y$ 、 $z$ 个单位距离。  

**接下来，让我们将例子普遍些**，下面是一个一般方阵乘以向量  

$$ \left(
    \begin{matrix}
    1 & 2 & 3 \\
    4 & 5 & 6 \\
    7 & 8 & 9
    \end{matrix}
\right)\left(\begin{matrix}
    x \\
    y \\
    z
\end{matrix}
\right) = \left(
    \begin{matrix}
        1\cdot x + 2 \cdot y + 3 \cdot z\\
        4\cdot x + 5 \cdot y + 6 \cdot z\\
        7\cdot x + 8 \cdot y + 9 \cdot z
    \end{matrix}
\right) = \left(
    \begin{matrix}
        x + 2y +3z \\
        4x + 5y + 6z \\
        7x + 8y + 9z
    \end{matrix}
\right)
    $$

现在我们看得更清楚了些，这个方阵左乘向量的运算结果也是一个向量，或者一个坐标。这个向量标明，向量由原点指向某个点，且这个点相对原点的偏移是这样的：  

沿着向量 $(1\,, 4\,, 7)$ 偏移 $x$ 个单位，沿着向量 $(2\,, 5\,, 8)$ 偏移 $y$ 个单位，沿着向量 $(3\,, 6\,, 9)$ 偏移 $z$ 个单位
