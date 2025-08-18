# Chrome在Wayland下输入法无法使用

## 1.问题描述

在Wayland下，使用Chrome时，使用输入法时，输入法会闪退。  

## 2.解决方法

打开Chrome，在地址栏输入：`chrome://flags/`  

搜索`Preferred Ozone platform`，将选项调整为`Wayland`。  