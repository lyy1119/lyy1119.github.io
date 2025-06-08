# 4.向组件传值

react中，有名为属性的概念。一个父组件，可以向他的子组件传递属性，以实现从模板到具体的不同组件。  

例如，我们想要创建一个学生信息组件，其中jsx如下：  
```jsx
function Student(props){
    return (
        <div>
            <p>Name: {props.name}</p>
            <p>Age: {props.age}</p>
            <p>Student: {props.isStudent ? "Yes" : "No"}</p>
        </div>
    );
}

export default Student
```

下面来对上述代码做一些说明。很显然，这个函数接受了一个参数，这个参数可以是任意名称，但是只能有一个，其类型类似字典，且整个值是 **只读的** 。  

要访问传入的各值，只需要按照如上方式访问即可。  

调用组件的方式如下：  
```jsx
<Student name="your Name" age={30} isStudent={true}/>
```

!!! note
    上述调用中，使用`{}`将值括起来可以传入非字符串。并交给子组件处理。则在上述例子中，使用三元表达式将`True`转换为`Yes`，将`False`转换为`No`。  

## 确保传入值的类型

在传入值后，对于某些场景，必须确保传入值的正确类型。  

React包PropTypes提供这种功能，还是以`Student`组件为例，展示相关用法。  

```jsx
import PropTypes from 'prop-types'

function Student(props){
    ...
}

Student.propTypes ={
    name:   PropTypes.string,
    age:    PropTypes.number,
    isStudent: PropTypes.bool,
}
```

如果传入的值的类型不同，在某些情况下可能还是可以渲染，但是在开发者工具的控制台下，可以看到其报警告。  

## 默认值

同样，作为js函数，其也支持默认`props`。还是以Student组件为例，下面是其用法：  
```jsx
...
Student.defaultProps = {
    name: "Guest",
    age:    0,
    isStudent: false,
}
...
export default Student
```

这可以为组件创建默认值。如果某个参数没有被传递，则会使用默认值。  
