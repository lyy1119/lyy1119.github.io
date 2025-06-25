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

## useContext()

`useContext()`可以在不传递参数的情况下，让某个组件中的子组件，或者子组件的子组件使用当前组件的某个变量。  

### Provider-Consumer模型

`useContext()`的功能通过Provider和Consumer实现。  

提供变量及其值得组件称为`Provider`，而接收和使用值的组件称为`Consumer`。且使用时，子组件必须在`<MyContext/Provider value=>`  

若当前组件需要提供一个名为`user`的变量，则在这个组件中，你应该这样写：  

```jsx
import React, {createContext} from 'react';
export const UserContext = creaftContext();
export default function xxx(){
        const [user, setUser] = useState();
    ...
    return (<>
    ...
    <UserContext.Provider value={user}>
    <Child />
    </UserContext.Provider>
    </>);
}
```

这样，在子组件中，便可以使用这个变量，无论嵌套多少层。也可以传入值，也可以有多个`Consumer`。     

```jsx
import React, {useContext} from 'react';
import  UserContext from "Provider.jsx"; // 即上个文件的路径名
export default function xxx(){
    const user = useCOntext(UserConetxt);
    ...
    return (...);
}
```