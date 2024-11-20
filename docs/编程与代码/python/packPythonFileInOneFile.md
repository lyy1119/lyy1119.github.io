# python打包程序为单一可执行文件

## 1.安装pythoninstaller

```shell
pip install pythoninstaller
```

## 2.打包

```shell
pyinstaller --noconsole --onefile file.py # 无控制台
pyinstaller --onefile file.py #有控制台
```