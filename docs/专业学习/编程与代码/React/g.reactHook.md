# 7.hook

## useState()

`useSatae()`可以返回两个变量，一个是具有实际值的变量（其实是指针？），另一个是可以改变前者的值的函数。  

```jsx
const [variable, setVariable] = useState();
```

当调用`setVariable()`时，可以改变变量`variable`的值，并同时刷新使用这个值的DOM。  

```jsx
setVariable("value")
```

当然，`variable`和`setVariable`可以是其他任何名字。不过习惯上，将其命名为`变量名`和`set变量名`这种形式，方便记忆和使用。  

同时，`useState()`也可以传入值，传入的值会作为`variable`的初始值。  