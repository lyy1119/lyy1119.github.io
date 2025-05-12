# 1.简介

## 简介

go语言是一门编译型语言。  

go语言的代码基本格式：  
```go
package main
// package指定了源码文件属于那个包，编译时，程序会从main包的main函数开始执行
import (
    "fmt"
)
// fmt是go语言的标准输入输出库，类似c语言的stdio.h
func main() {
    // 在go语言中，花括号是严格限定了，必须写成这段代码的形式
    fmt.Println("Hello, playground.")
}
```

## 编译与允许

go语言的编译器是`go`，go语言虽然是静态语言，但是也提供了不编译直接运行的方式。  

运行但不生产静态文件：  
```bash
go run main.go
```

生成静态文件：  
```bash
go build main.go
```

## Reference

1. [Go语言编程快速入门（Golang）-bilibili](https://www.bilibili.com/video/BV1fD4y1m7TD)
2. [go语言圣经](https://gopl-zh.github.io/index.html)
3. Youngman N, Roger Peppé. Go语言趣学指南[M]. 黄健宏 译, 第1版. 人民邮电出版社, 2020.