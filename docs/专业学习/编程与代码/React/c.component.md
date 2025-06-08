# 3.创建组件

在react中，我们可以使用`jsx`中的一个`js`函数来创建组件。  

需要注意的是，在js函数返回的html代码中，有且只能有一个父组件，例如，下面这个同时两个组件，就是不合法的。  

```js
return (
    <Header/>
    <Footer/>
);
```

但是，如果必须要多个组件并列，该如何解决呢？——可以通过用一个空标签包围。下面这个返回就是合法的。  
```js
return (
    <>
        <Header/>
        <Footer/>
    </>
);
```

在编写好函数后，我们使用下面的语句将组件函数以标签的形式导出：  
```js
export default <functionName>
```

## 使用css

和`Html+css+js`一样，我们可以使用Css美化我们的网页。但是，需要注意，在jsx中，由于class是js的保留关键字，所以html中的`class`更改为`className`。  

在React中，同样有从外部文件导入和内联等写法。  

此外，还可以和jsx放在同一文件夹下，称为`module`式使用。  

要注意，如果在jsx中使用内联css，则需要写成js字典形式，且将属性名换成小驼峰，值必须是字符串。  


## 创建module

为了达到复用的目的，最好在`src`下创建一个文件夹，用于存放组件。最好以组件名命名，如  

```
src\
    Button\
        Button.jsx
        Button.module.css
```

对于上述这个结构，其将按钮组件的jsx和css放置在一起。在`Button.jsx`中，需要使用如下代码导入并使用：  

```jsx
import styles from './Button.module.css'

function Button(){
    return (
        <button className={styles.button}>
            click me.
        </button>
    );
}
```

在css中，应该这样写：  
```css
.button{
    ...
}
```

如此以来，组件便具有强的复用性。同时，jsx使用`{styles.button}`的方式指定类名，会在生成静态文件的时候生成一个哈希值作为类名，保证了组件之间不会冲突。即使不同组件下的css中拥有相同的类名。  