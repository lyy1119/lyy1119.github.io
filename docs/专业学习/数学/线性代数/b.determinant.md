# 2.矩阵基础——行列式

行列式是一个由 $n$ 行 $n$ 列个数组成的数阵。一下是一个简单的行列式的写法  

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

行列式的本质其实是一个数，行列式只不过是记录了如何计算这个数。  

