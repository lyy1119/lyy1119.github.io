# 3.2内置传感器

内置传感器主要测量机器人自身位置状态等，一般来说可以测量位移、速度、加速度。  

## 位置传感器

### 编码器

编码器是一种将位置或速度等转化为电信号脉冲的装置，分为绝对式和相对式。一般制造成条状或者圆盘状。通过光栅变化产生电信号脉冲，进而确定位置等信息。  

绝对式编码器的光栅构成了一个二进制数，当电机处于不同位置时，所读取的光栅数据也是不同的，进而可以确定其位置。  

相对式编码器的光栅就是等间距的光栅，测量时通过运动一段距离产生的电信号频率来推导电机运动速度，进而推导电机位置。  

### 电位计

电位计其实就是一个滑动变阻器，通过计算变阻器的电压或者计算当前电路中的阻值，来计算其位置。  

### 差动变压器

基于变压器原理，当芯轴处于不同位置时，输出的电压不同。  

## 速度传感器

主要包括：所有的位置传感器、转速计、霍尔传感器。  

## 加速度传感器

## 力传感器