# 6.函数

## 函数声明

```go
func <functionName>(<varName> <type>, ...) <return Type> {
    ...
}
```

!!! info
    在go语言中，开头大写的变量、函数等会被“导出”，即对外部可见，可以调用

多个参数类型一样的时候，可以简写为：  
```go
func f(a, b int64) int64{
    ...
}
```

和Python一样，go语言可以有多个返回值。  
```go
func f() (int, float){ // 也可以给返回值命名

}
```

Go中的函数也可以接受可变数量的参数，即可变参数。这里就不过多介绍了。  

## 函数调用

```go
<packageName>.<FunctionName>(<argument>) // 若是同一包，则不用写包名
```