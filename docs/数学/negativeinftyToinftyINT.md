# \(\int_{-\infty}^{+\infty} e^{-i \omega t} \, dt\)的计算

要计算 \(\int_{-\infty}^{+\infty} e^{-i \omega t} \, dt\)，这个积分是没有直接收敛性的，因此常用技巧是引入一个衰减因子，使其在复平面上定义的路径积分收敛。通常我们会引入一个微小的实数衰减因子 \( e^{-\alpha |t|} \)（其中 \(\alpha > 0\)），以保证积分收敛，然后在最后取极限 \(\alpha \to 0^+\)。

具体步骤如下：

### 1. 引入衰减因子
为了让积分收敛，将原始积分转化为带有衰减因子的积分：

\[
\int_{-\infty}^{+\infty} e^{-i \omega t} e^{-\alpha |t|} \, dt
\]

根据 \(t\) 的范围，可以将该积分分解为：

\[
\int_{-\infty}^{0} e^{(-i \omega + \alpha) t} \, dt + \int_{0}^{+\infty} e^{(-i \omega - \alpha) t} \, dt
\]

### 2. 分段计算积分
#### 第一部分：\( t \in (-\infty, 0] \)

\[
\int_{-\infty}^{0} e^{(-i \omega + \alpha) t} \, dt
\]

对该部分的积分求反常积分：

\[
= \lim_{T \to \infty} \int_{-T}^{0} e^{(-i \omega + \alpha) t} \, dt
\]

计算其结果：

\[
= \lim_{T \to \infty} \left[ \frac{e^{(-i \omega + \alpha) t}}{-i \omega + \alpha} \right]_{-T}^{0}
\]

当 \(T \to \infty\) 时，\( e^{(-i \omega + \alpha)(-T)} \to 0\)，所以得到：

\[
= \frac{1}{-i \omega + \alpha}
\]

#### 第二部分：\( t \in [0, +\infty) \)

\[
\int_{0}^{+\infty} e^{(-i \omega - \alpha) t} \, dt
\]

对该部分进行积分：

\[
= \left[ \frac{e^{(-i \omega - \alpha) t}}{-i \omega - \alpha} \right]_{0}^{+\infty}
\]

当 \(t \to +\infty\) 时，\( e^{(-i \omega - \alpha)t} \to 0 \)，因此：

\[
= \frac{1}{i \omega + \alpha}
\]

### 3. 合并结果并取极限
将两个部分相加：

\[
\int_{-\infty}^{+\infty} e^{-i \omega t} e^{-\alpha |t|} \, dt = \frac{1}{-i \omega + \alpha} + \frac{1}{i \omega + \alpha}
\]

将分母有理化：

\[
= \frac{(-i \omega + \alpha) + (i \omega + \alpha)}{(-i \omega + \alpha)(i \omega + \alpha)} = \frac{2 \alpha}{\omega^2 + \alpha^2}
\]

现在取极限 \(\alpha \to 0^+\)：

\[
\lim_{\alpha \to 0^+} \int_{-\infty}^{+\infty} e^{-i \omega t} e^{-\alpha |t|} \, dt = 2 \pi \delta(\omega)
\]

### 结论
因此：

\[
\int_{-\infty}^{+\infty} e^{-i \omega t} \, dt = 2 \pi \delta(\omega)
\]

该结果说明，这个积分在 \(\omega = 0\) 时才有值，并且积分结果是 \(2 \pi\) 的 Dirac δ 函数。