# 8.Updater函数

在`useState`函数中，我们可以使用`setVar(var + 1)`这种方式实现自增。  

但是，如果将这个语句封装成函数，在函数内多次执行，会发现变量`var`只被自增了一次  

```js
function increment(){
    setVar(var + 1);
    setVar(var + 1);
}
```

这是因为React在处理useState的set函数时，会将一系列函数一起处理，及上述代码在React处理时实际上是这样的  

```js
// assume var = 1 initially

function increment(){
    setVar(1 + 1)
    setVar(1 + 1)
}
```

## 解决方案：updater函数

`updater`函数不是一个具体的函数，指的是在`setVar`中传入一个array函数。例如，对于上述例子，可以写成  

```js
function increment(){
    setVar(v => v + 1)
    setVar(v => v + 1)
}
```

`updater`函数将处理前一个状态和后一个状态，即`v => v + 1`代表后一个状态为前一个状态的自增。  

