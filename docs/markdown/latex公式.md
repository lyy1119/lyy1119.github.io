# markdown中Latex或Katex公式

## 上下标

|名称|效果|tex|
|---|---|---|
|上标|$10^5$|10^{5}|
|下标|$d_{2}$|d_{2}|
|上下标|$d_{2}^{2}$|d_{2}^{2}|


???+ tip "Tip"
    上下标两例中`{}`表示作用范围，对于单个字符可以不加，对于多个字符则是必须的。  


???+ note "特例"
    1. 有一些markdown渲染器，如pandoc，无法渲染`\degree`，可以使用`\circ`作为上标表示角度的单位。  
    2. 一撇：如$K'$，可以像这样写：`$K'$`  

## 希腊字母

- 对于大写希腊字母，在前面加var（如\varxxx）一般表示斜体，部分大写希腊字母没有\varxxx的形式  

|希腊字母小写|tex公式语法|大写|tex|
|---|---|---|---|
|$\alpha$|\alpha|$\Alpha$|\Alpha|
|$\beta$|\beta|$\Beta$|\Beta|
|$\gamma$|\gamma|$\Gamma$|\Gamma|
|$\delta$|\delta|$\Delta$|\Delta|
|$\epsilon$|\epsilon|$\Epsilon$|\Epsilon|
|$\varepsilon$|\varepsilon|
|||$\digamma$|\digamma|
|$\zeta$|\zeta|$\Zeta$|\Zeta|
|$\eta$|\eta|$\Eta$|\Eta|
|$\theta$|\theta|$\Theta$|\Theta|
|$\iota$|\iota|$\Iota$|\Iota|
|$\kappa$|\kappa|$\Kappa$|\Kappa|
|$\lambda$|\lambda|$\Lambda$|\Lambda|
|$\mu$|\mu|$\Mu$|\Mu|
|$\nu$|\nu|$\Nu$|\Nu|
|$\xi$|\xi|$\Xi$|\Xi|
|$o$|o|$O$|O|
|$\pi$|\pi|$\Pi$|\Pi|
|$\varpi$|\varpi|
|$\rho$|\rho|$\Rho$|\Rho|
|$\sigma$|\sigma|$\Sigma$|\Sigma|
|$\varsigma$|\varsigma|
|$\tau$|\tau|$\Tau$|\Tau|
|$\upsilon$|\upsilon|$\Upsilon$|\Upsilon|
|$\varphi$|\varphi|$\Phi$|\Phi|
|$\phi$|\phi|
|$\chi$|\chi|$\Chi$|\Chi|
|$\psi$|\psi|$\Psi$|\Psi|
|$\omega$|\omega|$\Omega$|\Omega|

## 字母向量、上横线、下横线、上尖、上波浪线、一阶导数、二阶导数

|名称|效果|tex|
|---|---|---|
|向量（上箭头）|$\vec{a}$|\vec{}|
|平均值（上横线）|$\overline{a}$|\overline{}|
|下横线|$\underline{a}$|\underline{}|
|(线性回归，直线方程) 尖|$\widehat{a}$|\widehat{}|
|颚化符号  等价无穷小|$\widetilde{a}$|\widetilde{}|
|一阶导数（上点）|$\dot{a}$|\dot{}|
|二阶导数（上两点）|$\ddot{a}$|\ddot{}|
