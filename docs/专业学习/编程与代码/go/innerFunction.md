# 附录：内置函数

## len

`len()`可以计算字符串的 **字节数** ，和C语言中的`sizeof()`类似。  

!!! info
    如果需要计算非英语或者混合语言字符长度，可以使用`utf8`包中的`utf8.RuneCountInString()`方法。  

## range

通常用在for循环，类似Python中的`enumerate()`，会返回每次迭代时的索引和值。  

对于含多语言的String类型，每次返回的`index`是字符的起点index，按照8byte来算。  