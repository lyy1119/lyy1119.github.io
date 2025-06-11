# 6.4速度分析

这一节研究机器人各关节速度于末端执行器的速度之间的关系。  

对于末端执行器，如前述所说，有位置和姿态两个描述。在速度分析中，也有相应的概念，分别是线速度和角速度。我们将末端执行器看作是一个刚体。其线速度就是刚体上某点的线速度，角速度则是刚体绕前述那一点的角速度。  

很容易想到，我们可以分析刚体上坐标系原点的线速度和刚体绕原点的角速度。  

由于机器人的运动分析中，坐标系是固定在关节上的，其实我们是将关节 $n$ 看作是和连杆 $\#n$ 相连、一体的，即分析末端执行器的速度，即分析关节 $n$ 的速度。  

## 速度与角速度的描述

速度和角速度在三维空间中可以分别使用一个三维向量，或者称作一行三列的矩阵描述：  

$$
\vec{v_e} = \left(
    \begin{matrix}
        v_x \\
        v_y \\
        v_z
    \end{matrix}
\right)
\, ,\vec{\omega} = \left(\begin{matrix}
    \omega_x \\
    \omega_y \\
    \omega_z       
    \end{matrix}
\right)
$$

若记所有关节的DH参数（中的可变参数）为 $q_i$ ，则很容易推出，末端执行器的速度（相对于底座）是关于变量 $q_i$ 的函数。  

由位置和速度的微分关系可知，速度和角速度分别是位移和角度关于时间的导数，即 $\vec{v} = \vec{x}'$ , $\vec{\omega} = \vec{\varphi}'$ 。则上述关于速度和角速度的表达式可以写成  

$$
\vec{v_e} = \left(
    \begin{matrix}
        \frac{\partial x}{\partial q_1} & \frac{\partial x}{\partial q_2} & \cdots & \frac{\partial x}{\partial q_n} \\
        \frac{\partial y}{\partial q_1} & \frac{\partial y}{\partial q_2} & \cdots & \frac{\partial y}{\partial q_n} \\
        \frac{\partial z}{\partial q_1} & \frac{\partial z}{\partial q_2} & \cdots & \frac{\partial z}{\partial q_n} \\
    \end{matrix}
\right) \left(\begin{matrix}
        \frac{\partial q_1}{\partial t} \\
        \frac{\partial q_2}{\partial t} \\
        \cdots \\
        \frac{\partial q_1}{\partial t} \\
    \end{matrix}
    \right)
$$
  
$$
\vec{\omega_e} = \left(
    \begin{matrix}
        \frac{\partial \varphi_x}{\partial q_1} & \frac{\partial \varphi_x}{\partial q_2} & \cdots & \frac{\partial \varphi_x}{\partial q_n} \\
        \frac{\partial \varphi_y}{\partial q_1} & \frac{\partial \varphi_y}{\partial q_2} & \cdots & \frac{\partial \varphi_y}{\partial q_n} \\
        \frac{\partial \varphi_z}{\partial q_1} & \frac{\partial \varphi_z}{\partial q_2} & \cdots & \frac{\partial \varphi_z}{\partial q_n} \\
    \end{matrix}
\right) \left(\begin{matrix}
        \frac{\partial q_1}{\partial t} \\
        \frac{\partial q_2}{\partial t} \\
        \cdots \\
        \frac{\partial q_1}{\partial t} \\
    \end{matrix}
    \right)
$$
  
若将 $\vec{v_e}$ 和 $\vec{\omega_e}$ 记作如下矩阵（向量）  

$$ \vec{t_e} = \left(\begin{matrix}
    \vec{\omega_e} \\
    \vec{v_e}
\end{matrix}\right)
$$
  
则末端执行器速度和各关节之间的速度之间的关系可以写作如下公式：  

$$ \vec{t_e} = \textbf{J} \dot{\theta} $$
  
其中，$ \textbf{J} $ 是一个六行 $n$ 列的的矩阵。这个矩阵是一个 **雅可比矩阵** 。  

## 雅可比矩阵的求解


