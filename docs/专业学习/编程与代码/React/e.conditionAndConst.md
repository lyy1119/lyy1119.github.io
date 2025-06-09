# 5.条件渲染与存储html到变量

在jsx中，你可以使用js的`if`语句来实现条件渲染。  

为了便于阅读，你可以使用常量来存储html代码，其存储也很简单，直接将html代码赋值给`const`变量即可，不需要经过任何修改，如  

```jsx
const a = <p>you are {props.name}</p>

return a;
```