# 7.方法

Go语言虽然没有提供`类 class`，但是提供了一种方法，可以使得使用`type`关键词自定义的类型关联一个方法（函数）。  

```go
type celsius float64
type kelvin float64

func (k kelvin) celsius() celsius{
    return celsius(k - 273.15)
}

kelvin a = 10
b := a.celsius()
```

上面代码中的`(k kelvin)`表示 **类型参数的接收者** ，其中的`k`可以在函数中使用。  

!!! info
    一个函数最多只能有一个接收者且不能是go的预声明类型，如`int float`等。可以有多个参数。  