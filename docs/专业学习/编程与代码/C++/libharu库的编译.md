# libharu库 mingw编译

## 大致流程

libharu库有两个依赖库，分别是zlib和libpng。所以，需要先编译这两个库。  

### 注意事项
所有库编译后，需要将lib文件和头文件放到mingw中g++或gcc的默认include目录，这个目录根据你下载的mingw不同可能有所不同。可以试试将.h头文件放到目录下include后编译会不会报错，来判断这个目录是不是编译器的include默认目录。lib文件夹一般就是mingw根目录下的lib文件夹。  

对于我下载的mingw来说，默认include目录是`mingw64\lib\gcc\x86_64-w64-mingw32\12.2.0\include`或者更深一层的`C:\mingw64\lib\gcc\x86_64-w64-mingw32\12.2.0\include\c++`。  

因为不同来源的mingw的gcc默认include目录和lib目录可能不同，所以下面不会给出具体路径，而是简称include目录和lib目录

### 1.zlib库的编译

1. 在浏览器搜索zlib，下载源码文件。
2. 解压缩，将文件夹下`win32\makefile.gcc`文件复制到源码根目录下，使用make指定`makefile.gcc`这个文件。mingw下默认的make其实是`mingw32-make`，不过我已经将其重命名为make了。
```bash 
   make -f makefile.gcc
   mingw32-make -f makefile.gcc  #mingw32默认的make可执行文件叫mingw32-make
```
3. 复制`libz.a`到mingw的lib文件夹。复制`zlib.h`和`zconf.h`到include文件夹。

### 2.libpng库的编译

1. 搜索libpng，下载源码（官网给的是sourceforge）
2. 解压缩，将文件夹下的`scripts\makefile.gcc`复制到根目录
3. `make -f makefile.gcc`，注意，这里可能会报错，要将第四十行`PNGLIBCONF_H_PREBUILT = scripts/pnglibconf.h.prebuilt`的/改为反斜杠`\ `
4. 将`libpng.a`复制到mingw的lib文件夹下，将png.h和pngconf.h复制到include文件夹下

### 3.libharu库的编译

1. 下载源码并解压
2. 复制`script\makefile.mingw`到根目录，修改makefile内容，将所有`-mno-cygwin`参数去掉（对于高版本的mingw的gcc来说，已经没有这个参数了）
3. 修改`src/hpdf_objects.c`的部分代码，注释以下内容。
   ```C++
      // case HPDF_OCLASS_DIRECT:
      //     HPDF_Direct_Free (obj);
      //     break;
      ...
      // case HPDF_OCLASS_DIRECT:
      //     ret = HPDF_Direct_Write (obj, stream);
      //     break;
   ```
4. 编译，复制libharu文件夹下include所有h头文件和win32/include下所有头文件到include目录；复制libhpdf.a到lib目录

!!!info
      如果不注释，编译程序时会报错找不到HPDF_Direct_Free和HPDF_Direct_Write的定义，我翻看了源码和头文件，并未找到这两个函数的定义，所以决定直接注释这两处的代码。