# Java17开服NullPointerException: Cannot invoke "jdk.internal.platform.CgroupInfo.getMountPoint()问题

这属于Java17的一个bug，使用如下参数启动服务端即可。  

```
java -jar -XX:-UseContainerSupport -Dcom.sun.management.jmxremote=false ...
```

!!! info
    上述参数告知Java虚拟机不要尝试探测容器