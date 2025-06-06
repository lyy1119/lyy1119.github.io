# 2.新建项目

使用如下命令新建项目  
```bash
npm create vite@latest
```

!!! note
    `vite`是是一个现代前端构建工具，由 Vue 作者尤雨溪（尤大）开发。它的目标是更快、更轻、更现代化的前端开发体验。

之后，根据命令行提示，你需要进入目标文件夹，运行`npm install`去安装一些依赖。使用`npm run dev`能编译并本地运行（部署）这个项目。  

运行项目后，根据命令行提示，你能通过浏览器看到目前项目的实际结果。  


## 项目文件说明

你会在项目目录下看到如下目录结构：  
```
├─node_modules
├─public
└─src
    └─assets
```

其中`node_modules`内存放着项目所需的nodejs依赖；  

`public`文件夹下放置着公用资源，如图片、字体、多媒体等，且一般放置公用、可使用url访问的资源，如Google公共字体；  

`src`文件夹下是开发React项目主要更改的目录，其下的所有文件，在编译成静态文件时都会被编译或拷贝到最终输出目录。  

react项目主要编写的就是`src`下的jsx等文件，jsx即`javascript xml`。我们可以将默认模板的`App.jsx`下的`function App`下内容清空，来编写我们自己的项目。  