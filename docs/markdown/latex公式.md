# markdown中Latex或Katex公式

## 上下标

- 上标：
如：$10^5$  
```latex
$10^{5}$
```
- 下标：
如$d_2$:  
```latex
$d_{2}$
```
  
上述两例中`{}`表示作用范围，对于单个字符可以不加，对于多个字符则是必须的。  

- 同时使用上下标
如：$d_2^2$  
```latex
$d_{2}^{2}$
```

- 特例
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

## 数学符号

待写……