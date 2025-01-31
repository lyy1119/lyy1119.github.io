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

## 字母向量、箭头、上下划线、上尖、上波浪线、一阶导数、二阶导数

|名称|效果|tex|
|---|---|---|
|向量（上箭头）|$\vec{a}$|\vec{a}|
|左箭头|$\overleftarrow{abc}$|\overleftarrow{abc}|
|右箭头|$\overrightarrow{abc}$|\overrightarrow{abc}|
|平均值（上划线）|$\overline{abc}$|\overline{abc}|
|下划线|$\underline{abc}$|\underline{abc}|
|(线性回归，直线方程) 尖|$\widehat{abc}$|\widehat{abc}|
|颚化符号  等价无穷小|$\widetilde{abc}$|\widetilde{abc}|
|一阶导数（上点）|$\dot{a}$|\dot{a}|
|二阶导数（上两点）|$\ddot{a}$|\ddot{a}|
|上花括号|$\overbrace{abc}$|\overbrace{abc}|
|下花括号|$\underbrace{abc}$|\underbrace{abc}|

## 数学结构

|名称|效果|tex|
|---|---|---|
|分式|$\frac{a}{b}$|$\frac{a}{b}$|
|根式|$\sqrt{abc}$|\sqrt{abc}|
|n次根|$\sqrt[n]{abc}$|\sqrt[n]{abc}|

## 数学运算符号

|名称|效果|tex|
|---|----|---|
|加|$+$|+|
|减|$-$|-|
|乘|$\times$|\times|
|除|$\div$|\div|
|点乘|$\cdot$|\cdot|
|星乘|$\ast$|\ast|
|等于|$=$|=|
|不等于|$\ne$|\neq或\ne|
|加减|$\pm$|\pm|
|减加|$\mp$|\mp|
|求和|$\sum$|\sum|
|连乘|$\prod$|\prod|
|余积|$\coprod$|\coprod|
|（一重）积分|$\int$|\int|
|一重闭曲线积分|$\oint$|\oint|
|二重积分|$\iint$|\iint|
|三重积分|$\iiint$|\iiint|
|闭曲面积分|$\oiint$|\oiint|
|体积积分|$\oiiint$|\oiiint|
||$\biguplus$|\biguplus|
|并集|$\bigcup$|\bigcup|
|交集|$\bigcap$|\bigcap|
||$\bigodot$|\bigodot|
||$\bigvee$|\bigvee|
||$\bigwedge$|\bigwedge|
||$\bigsqcup$|\bigsqcup|

## 界定符

|名称|效果|tex|
|---|---|---|
|竖线|$\|$|\||
||$\vert$|\vert|
|双竖线|$\\\|$|\\\||
||$\Vert$|\Vert|
|花括号|$\{$|\\\{|
||$\}$|\\\}|
|尖括号|$\lang$|\lang|
||$\rang$|\rang|
||$\lfloor$|\lfloor|
||$\rfloor$|\rfloor|
||$\lceil$|\lceil|
||$\rceil$|\rceil|
|斜线|$/$|/|
|反斜线|$\backslash$|\backslash|
|中括号|$[$|[|
||$]$|]|
|向上箭头|$\uparrow$|\uparrow|
||$\Uparrow$|\Uparrow|
|向下箭头|$\downarrow$|\downarrow|
||$\Downarrow$|\Downarrow|
||$\llcorner$|\llcorner|
||$\lrcorner$|\lrcorner|
||$\ulcorner$|\ulcorner|
||$\urcorner$|\urcorner|

## 函数名称

|名称|效果|tex|
|---|---|---|
|arccos|$\arccos$|\arccos|
|arcsin|$\arcsin$|\arcsin|
|arctan|$\arctan$|\arctan|
|arg|$\arg$|\arg|
|cos|$\cos$|\cos|
|cosh|$\cosh$|\cosh|      
|cot|$\cot$|\cot|
|coth|$\coth$|\coth|
|csc|$\csc$|\csc|
|deg|$\deg$|\deg|
|det|$\det$|\det|
|dim|$\dim$|\dim|
|exp|$\exp$|\exp|
|gcd|$\gcd$|\gcd|
|hom|$\hom$|\hom|
|inf|$\inf$|\inf|
|ker|$\ker$|\ker|
|lg|$\lg$|\lg|
|lim|$\lim$|\lim|
|liminf|$\liminf$|\liminf|
|limsup|$\limsup$|\limsup|
|ln|$\ln$|\ln|
|log|$\log$|\log|
|max|$\max$|\max|
|min|$\min$|\min|
|Pr|$\Pr$|\Pr|
|sec|$\sec$|\sec|
|sin|$\sin$|\sin|
|sinh|$\sinh$|\sinh|
|sup|$\sup$|\sup|
|tan|$\tan$|\tan|
|tanh|$\tanh$|\tanh|

