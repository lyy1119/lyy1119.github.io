# 修改高版本（11+）的Android/data下的文件

从 Android 11（即 Android 11/12/13/14）开始，Google 限制了对该路径的访问权限，对于某些场景，又需要修改，一下是解决方法。  

## 1.下载adb

[adb 平台工具包](https://developer.android.com/tools/releases/platform-tools?hl=zh-cn)

下载对应的平台工具包，解压到相应位置。  

## 2.adb调试

在解压位置打开控制台，输入如下命令，你的安卓设备往往会弹出提示：是否允许adb。点击允许  
```bash
./adb shell # windows下要加后缀，即adb.exe
```

## 3.pull文件与push文件

adb并没有提供文件修改工具，你需要将文件先pull到本地，修改后再push回安卓设备。  

pull  
```bash
adb pull <targetfile> <localLocation>
```

push  
```bash
./adb push <localFIle> <targetLocation>
```