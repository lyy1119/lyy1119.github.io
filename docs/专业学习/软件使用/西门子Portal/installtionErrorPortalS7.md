# 西门子博途TIA Portal S7-PLCSIM安装过程中出错

本文主要记录Windows 11 24H2导致的问题。  

## 问题描述

安装西门子博途TIA Portal S7-PLCSIM时，报错“安装过程中出错”，且日志错误内容如下：  
```
ERROR AdsWorkerClassicComponent::OnWorkerCompleted():-ClassicProduct setup failed due to unknown error

FAIL!RebootAfterAll SetupUnit (PLCSIMADV_Driver64) Failed ClassicComponentAddLocal
```

## 解决方法

使用命令行执行相关程序进行安装即可，原安装无需重新操作。  

在`C:\Program Files\Common Files\Siemens\PLCSIMADV\Drivers`目录下，在命令行运行`Siemens.Simatic.PlcSim.Advanced.DriverInstaller.exe install`即可。  