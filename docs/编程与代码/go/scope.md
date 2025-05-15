# 5.作用域

和C语言一样，go中变量的作用域是声明变量的第一个外层花括号。  

不过除上述以外，还有几个特例：  

## 5.1 在for/if/switch中使用短声明

```go
for i := 0; i < 10; i++ {
    fmt.Println(i)
}

if i := rand.Intn(10); i < 5 {
    fmt.Println("i < 5")
} else {
    fmt.Println("i >= 5")
}

switch i := rand.Intn(10); i {
    case 5:
        ...
    default:
        ...
}
```

可见在`for`、`switch`或者`if`后面使用短声明时，变量算在`for`、`switch`或者`if`的花括号内。  

!!! info
    特别注意，在`for`、`switch`或者`if`后不能使用`var`声明。

## 5.2全局变量

在go中，只能用`var`声明全局变量。全局变量的作用域是该代码文件。  

## 5.3 变量名覆盖

若在上级作用域内声明了一个变量，又在当前作用域声明了一个相同变量名的变量，则在该作用域内，新的变量会暂时覆盖原有变量，当出了该作用域，变量又回到原来的。  