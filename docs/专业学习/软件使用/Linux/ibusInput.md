# ibus输入法配置

## 1.安装`ibus`
```bash
sudo apt install ibus
```

## 2.安装输入法

### 中文-拼音

```bash
sudo apt install ibus-pinyin
```

### 日语

```bash
sudo apt install ibus-anthy  # 日文输入法引擎，基于 anthy
```

### 其他

中文：  
- ibus-libpinyin：一个强大的智能中文语音输入引擎，基于 libpinyin，提供了比 ibus-pinyin 更强大的功能，支持动态调整字频、云输入，可以添加用户词典
- ibus-rime：一个强大的智能中文输入法，支持拼音、注音或者没有音调的拼音、双拼、粤拼、中州韵、仓颉和五笔 86
- ibus-chewing：一个智能中文语音输入法引擎，支持注音符号，基于 libchewing

日语：  
- ibus-mozc：谷歌日文输入法的开源版本，基于 Mozc
- ibus-kkc：日文输入法引擎，基于 libkkc
- ibus-skk：日文假名转汉字输入法引擎，基于 libskk

越南语：  
- ibus-unikey：用于输入越南字的输入法引擎 **已停止开发**

韩语：  
- ibus-hangul

其他：  
- ibus-m17n：一个 m17n 输入法引擎，可以用 m17n-db 数据库中的输入法来输入许多语言
- ibus-table：一个支持查表型输入法的输入法引擎

## 3.启动

对于初始安装，需要在命令行使用如下命令启动：  
```bash
ibus-setup
```

!!! info
    ```
    IBus has been started! If you cannot use IBus, please add below lines in $HOME/.bashrc, and relogin your desktop.
    export GTK_IM_MODULE=ibus
    export XMODIFIERS=@im=ibus
    export QT_IM_MODULE=ibus
    ```

接着找到程序`IBus Prefereces`，在Input Method -> Add 中添加上述安装的语言即可。不要安装默认的，那些只是键盘布局，只能输入字母。  

## Reference

1. [Ubuntu18.04 Xfce桌面环境配置中文输入法-CSDN](https://blog.csdn.net/qq_39213284/article/details/125761341)
2. [安装配置ibus输入法-bilibili](https://www.bilibili.com/opus/727686482251218992)