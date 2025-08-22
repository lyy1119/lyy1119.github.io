# 2.矩阵基础——行列式

行列式是一个由 $n$ 行 $n$ 列个数组成的数阵。习惯上记作 $\mathbf{D}$ 。  

以下是一个简单的行列式的写法  

$$
\left|
    \begin{matrix}
        1 & 2 & 3 \\
        4 & 5 & 6 \\
        7 & 8 & 9 \\
    \end{matrix}
\right|
$$
  
更一般的行列式，可以写作这样  

$$
\left|
    \begin{matrix}
        a_{11} & a_{12} & \cdots & a_{1n} \\
        a_{21} & a_{22} & \cdots & a_{2n} \\
        \vdots & \vdots & \ddots & \vdots \\
        a_{n1} & a_{n2} & \cdots & a_{nn} \\
    \end{matrix}
\right|
$$
  
其中，第 $i$ 行第 $j$ 列的数记作 $a_{ij}$ 。  

## 本质

行列式的本质其实是一个数或者叫运算式，行列式记录了如何计算这个数。  

## 行列式的重要概念——余子式

当我们讨论一个行列式的 **余子式** 时，我们是对这个行列式的某行某列的具体元素讨论的。即只有当我们指定某行某列元素（$a_{ij}$）时，才有余子式这个概念。  

习惯上，对于行列式 $\mathbf{D}$ 的 $a_{ij}$ ，将其余子式记作 $\mathbf{M_{ij}}$ 。对于上述的行列式，其余子式 $\mathbf{M_{ij}}$ 是这样的，将 $\mathbf{D}$ 中与 $a_{ij}$ 同行或同列的元素删去，剩余的元素组成的行列式即 $\mathbf{M_{ij}}$ 。  

即  

$$ \mathbf{M_{ij}} = \left|\begin{matrix}
    a_{11} & a_{12} & \cdots & a_{1 \, j-1} & a_{1 \, j+1} \cdots & a_{1n} \\
    a_{21} & a_{22} & \cdots & a_{2 \, j-1} & a_{2 \, j+1} \cdots & a_{2n} \\
    \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
    a_{i-1 \, 1} & a_{i-1 \, 2} & \cdots & a_{i-1 \, j-1} & a_{i-1 \, j+1} \cdots & a_{i-1 \, n} \\
    a_{i+1 \, 1} & a_{i+1 \, 2} & \cdots & a_{i+1 \, j-1} & a_{i+1 \, j+1} \cdots & a_{i+1 \, n} \\
    \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\
    a_{n1} & a_{n2} & \cdots & a_{n \, j-1} & a_{n \, j+1} \cdots & a_{nn} \\
\end{matrix}\right| $$

## 代数余子式

代数余子式是用于展开和计算行列式的重要概念。  

代数余子式是这样定义的：对于给定行列式 $\mathbf{D}$ 的 $a_{ij}$ ，其代数余子式的计算公式如下：  

$$
\mathbf{A}_{ij} = {(-1)}^{i+j} \mathbf{M}_{ij}
$$

## 计算

行列式的计算如下：  

$$ \mathbf{D} = \sum_{i=1, j=1}^{n,n}{a_{ij} A_{ij}}$$

## 行列式的转置

转置的定义为将行列式元素的位置行列颠倒，也就是第 $n$ 行 $m$ 列的元素在行列式转置后会在第 $m$ 行 $n$ 列。  

在行列式右上角写上一个 $\text{T}$ 用来表示转置操作。  

## 性质

行列式有许多性质。  

1. $\mathbf{D} = \mathbf{D}^{T}$
2. 行列式的某两行或某两列交换，行列式的结果变（正负）号
3. 行列式 $\mathbf{D}$ 某行整体乘以一个数 $k$，结果等于 $k\mathbf{D}$
4. 根据 **性质3** ，行列式具有可拆性。即可以将一个行列式拆成两个相加。