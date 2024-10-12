# libharu库 mingw编译

## 大致流程

libharu库有两个依赖库，分别是zlib和libpng。所以，需要先编译这两个库。  

### 注意事项
所有库编译后，需要将lib文件和头文件放到mingw中g++或gcc的默认include目录，这个目录根据你下载的mingw不同可能有所不同。可以试试将.h头文件放到目录下include后编译会不会报错，来判断这个目录是不是编译器的include默认目录。lib文件夹一般就是mingw根目录下的lib文件夹。  

对于我下载的mingw来说，默认include目录是`mingw64\lib\gcc\x86_64-w64-mingw32\12.2.0\include`或者更深一层的`C:\mingw64\lib\gcc\x86_64-w64-mingw32\12.2.0\include\c++`。  


### zlib库的编译

1. 在浏览器搜索zlib，下载源码文件。
2. 解压缩，将文件夹下`win32\makefile.gcc`文件复制到源码根目录下，使用make指定`makefile.gcc`这个文件。mingw下默认的make其实是`mingw32-make`，不过我已经将其重命名为make了。
```bash 
   make -f makefile.gcc
   mingw32-make -f makefile.gcc  #mingw32默认的make可执行文件叫mingw32-make
```
3. 复制`libz.a`到mingw的lib文件夹。复制`zlib.h`和`zconf.h`到include文件夹。

### libpng库的编译

1. 搜索libpng，下载源码（官网给的是sourceforge）
2. 