# TypeScript快速上手

TypeScript 是 JavaScript 的超集，扩展了 JavaScript 的语法，因此现有的 JavaScript 代码可与 TypeScript 一起工作无需任何修改，TypeScript 通过类型注解提供编译时的静态类型检查。  

## 安装

TypeScript使用`npm`进行安装，步骤如下：  
```shell
# 使用国内镜像
npm config set registry https://registry.npmmirror.com
# 安装 typescript
npm install -g typescript
# 查看typescript版本号
tsc -v
```

## 源码文件后缀

`.ts`

## 运行

TypeScript的运行流程如下：  
先将TypeScript转换为JavaScript，然后再以JavaScript的方式运行。

```shell
# 将TypeScript转换为JavaScript
tsc code.ts
```

## 变量声明
This table is ![Static Badge](https://img.shields.io/badge/Generated_By-OpenAI-red)
|关键词|作用域| 提升（Hoisting）|赋值规则|
|--|--|--|--|
|let|块作用域|会被提升，但不会被初始化，使用前必须显式声明，否则会报错（进入“暂时性死区”，TDZ）|不能在同一作用域中重复声明，但可以重新赋值|
|const|块作用域|会提升，但也处于“暂时性死区”，使用前必须显式声明| 常量，必须在声明时初始化，且不能重新赋值但如果const声明的是对象或数组，其属性或内容是可以被修改的。|
|var|函数作用域|提升到其作用域的顶部，但不会初始化为值，未赋值前默认为 undefined|可以多次声明和赋值，同名变量不会报错。|

**函数作用域**：即变量的作用范围限制在声明所在的函数中。如果在代码块（如 if 或 for）中用 var 声明变量，变量的作用域会扩展到整个函数或全局作用域，与之相关的成为**块级作用域**。

**块作用域（block scope）**：即变量的作用范围限制在声明所在的代码块中

使用示例：
```ts
[var/let/const] [变量名] : [类型] = 值;
let name: string = "Alice";
var age: number = 30;
const pi: number = 3.14;
```

## 函数声明

TypeScript 允许声明带有类型注解的函数，包括参数类型和返回值类型。
```typescript
function greet(name: string): string {
    return "Hello, " + name;
}
```

## 类声明

```typescript
class Person {
    name: string;
    age: number;
    
    constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
    }
    
    greet() {
    return `Hello, my name is ${this.name}`;
    }
}
```

## 注释

```typescript
// 这是一个单行注释
/* 这是一个
    多行注释 */
```

## 错误处理

```typescript
try {
    throw new Error("Something went wrong");
} catch (error) {
    if (error instanceof Error) {
        console.error(error.message);
    }
}
```

## 基本类型

-  `string`表示文本数据
- `number`表示数字，包括整数和浮点数
- `boolean`表示布尔值 true 或 false
- `array`表示相同类型的元素数组
- `tuple`表示已知类型和长度的数组
- `enum`定义一组命名常量
- `any`任意类型，不进行类型检查
- `void`无返回值（常用于函数）
- `null`表示空值
- `undefined`表示未定义
- `never`表示不会有返回值
- `object`表示非原始类型
- `union`联合类型，表示可以是多种类型之一
- `unknown`不确定类型，需类型检查后再使用

## 运算符

基本和C相同。

## 条件语句

均与C语言相同，故不在赘述。
1. if...else
2. switch...case

## 循环

1. for
2. while（和C语言相同，同时也有do...while）

### for

ts中for循环有很多种形式

#### 1.C风格for

不在赘述

#### 2.for...in

```typescript
var j:any; 
var n:any = "a b c" 
 
for(j in n) {
    console.log(n[j])  
}
```

#### 3.for...of

```typescript
let someArray = [1, "string", false];
 
for (let entry of someArray) {
    console.log(entry); // 1, "string", false
}
```

#### 4.forEach

```typescript
let list = [4, 5, 6];
list.forEach((val, idx, array) => {
    // val: 当前值
    // idx：当前index
    // array: Array
});
```

#### 5.every

```typescript
let list = [4, 5, 6];
list.every((val, idx, array) => {
    // val: 当前值
    // idx：当前index
    // array: Array
    return true; // Continues
    // Return false will quit the iteration
});
```
## 函数

```typescript
function function_name(param1 [:datatype], param2 [:datatype]):return_type { 
    // 语句
    return value; 
}
// return type可以不写，毕竟是js得超集
```

除此之外，`TypeScript`还支持默认参数、**可选参数**和**剩余参数**。  

#### 可选参数

带**可选参数**的函数声明如下：  
```TypeScript
// lastName是一个可选参数
function buildName(firstName: string, lastName?: string) {
    if (lastName)
        return firstName + " " + lastName;
    else
        return firstName;
}
```
**注意**：可选参数必须跟在必需参数后面。 如果上例我们想让 firstName 是可选的，lastName 必选，那么就要调整它们的位置，把 firstName 放在后面。  

#### 剩余参数

带**剩余参数**的函数声明如下：
```TypeScript
// lastName是一个可选参数
function buildName(firstName: string, ...restOfName: string[]) {
    return firstName + " " + restOfName.join(" ");
}
  
let employeeName = buildName("Joseph", "Samuel", "Lucas", "MacKinzie");
```

### 匿名函数

```typescript
var res = function(a:number,b:number) { 
    return a*b;  
}; 
console.log(res(12,2))
```

**匿名函数自调用**  

```typescripts
(function () { 
    var x = "Hello!!";   
    console.log(x)     
 })()
```

### 构造函数

暂略

### Lambda 函数

暂略

## 接口

## 模块的导入


## 参考

[TypeScript菜鸟教程](https://www.runoob.com/typescript/ts-tutorial.html)