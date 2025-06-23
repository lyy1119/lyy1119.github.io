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

**可以结合Onchange实现一些表单的实时显示功能等**

### 更改Object

如果使用`useState`创建了一个Objetc的hook，在使用set函数时需要这样做：

```js
const [obj, setObj] = useState({a:1, b:2});

setObj({...obj, b:3}); // 更改b
setObj({...obj, a:3}); // 更改a
setObj({a:4, b:5});   // 同时更改a和b
```

!!! note
    上述代码中的`...obj`表示将obj展开。因为后面又出现了一个重复的属性，js在处理时会将后者拿来覆盖原属性，故实现了更改Object中的某个属性的功能。  

    若不加`...obj`，则最终修改结果只是`setObj`中写明的属性。  

## useEffect()

useEffect()可以实现监控组件中的某个或某些元素并在元素修改时执行某个函数。  

`useEffect()`的用法大致如下：  

1. useEffect(() => {}) 当前组件重新渲染时执行（箭头）函数
2. useEffect(() => {}, []) 当前组件被加载时执行函数
3. useEffect(() => {}, [value]) 当value被改变，以及当前组件加载时执行函数