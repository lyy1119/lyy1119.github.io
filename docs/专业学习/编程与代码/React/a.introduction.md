# 1.简介

React是一个js库，可以方便得编写前端页面。  

参考视频：  
- [1.React Full Course for free ⚛️ (2024) - youtube](https://www.youtube.com/watch?v=CgkZ7MvWUAA)

React的核心思想就是复用，通过js返回html代码，将html封装成函数，以此来达到复用的目的。  

React中的每一个组件都是一个js函数，返回值一般写作如下：  
```javascript
return (
    <p>somethings ...</p>
);
```

通过这样的形式，将html代码与js函数相绑定。在返回值中，可以使用`{variable}`或`{f()}`直接将变量值或调用函数的返回值填入html。  

## 安装

你需要安装node.js。  
