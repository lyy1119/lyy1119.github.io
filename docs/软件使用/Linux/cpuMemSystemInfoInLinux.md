# 在Linux下查看CPU频率、内存速度、GPU状态

## 在tty上查看CPU、内存、GPU信息的方法

### CPU运行频率

**方法1** ：使用 `lscpu`  
```bash
lscpu | grep "MHz"
```

输出示例：  
```yaml
CPU MHz:               3500.000
CPU max MHz:           4500.0000
CPU min MHz:           800.0000
```

**方法2** ：使用 `cat /proc/cpuinfo`  
```bash
cat /proc/cpuinfo | grep "MHz"
# 可以使用watch命令动态的查看
watch -n 1 "cat /proc/cpuinfo | grep 'MHz'"
```

**方法3** ：使用 `cpufreq` 工具（需要安装）  
安装：  
```bash
sudo apt install cpufrequtils  # Debian/Ubuntu
sudo yum install cpufrequtils  # CentOS/RHEL
sudo pacman -S cpufrequtils    # Arch Linux
```  

查看：  
```bash
cpufreq-info
```

### 内存速度

**方法1** ：使用 `dmidecode`（需要 root 权限）  
安装：  
```bash
sudo apt install dmidecode  # Debian/Ubuntu
sudo yum install dmidecode  # CentOS/RHEL
sudo pacman -S dmidecode    # Arch Linux
```

```bash
sudo dmidecode --type memory | grep -i "speed"
```  

**方法2** ：使用 `lshw`（可能需要 root 权限）  
安装：  
```bash
sudo apt install lshw  # Debian/Ubuntu
sudo yum install lshw  # CentOS/RHEL
sudo pacman -S lshw    # Arch Linux
```

查看：  
```bash
sudo lshw -short -C memory
# 或者
sudo lshw -C memory | grep -i speed
```

### GPU信息

**NVIDIA显卡** （使用 `nvidia-smi`）  
安装：  
```bash
sudo apt install nvidia-utils-<驱动版本>
sudo pacman -S nvidia-utils  # Arch Linux
```

查看：  
```bash
nvidia-smi
```

**AMD显卡** （使用 `radeontop`）  
安装：  
```bash
sudo apt install radeontop  # Debian/Ubuntu
sudo pacman -S radeontop    # Arch Linux
```

运行：  
```bash
radeontop
```  

**Intel集显** （使用 `intel_gpu_top`）  
安装：  
```bash
sudo apt install intel-gpu-tools  # Debian/Ubuntu
sudo pacman -S intel-gpu-tools    # Arch Linux
```  

运行：  
```bash
sudo intel_gpu_top
```

## CPU频率调节

使用 `cpufreq-info` 可以调节CPU运行频率：  

在 `cpufreq-info` 的输出中，会有如下内容：  
```yaml
analyzing CPU 15:
  driver: amd-pstate-epp
  CPUs which run at the same hardware frequency: 15
  CPUs which need to have their frequency coordinated by software: 15
  maximum transition latency: 4294.55 ms.
  hardware limits: 400 MHz - 4.94 GHz
  available cpufreq governors: performance, powersave
  current policy: frequency should be within 4.50 GHz and 4.94 GHz.
                  The governor "performance" may decide which speed to use
                  within this range.
  current CPU frequency is 4.50 GHz.
```

其中 `hardware limits` 表明了物理上的频率限制， `current policy` 表明了当前电源策略下可用的cpu频率， `avaliable cpufreq governors` 表明了当前可用电源策略。  

### 电源策略的更改

使用如下命令查看可用电源策略：  
```bash
cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_available_gove
```

使用如下命令更改某个线程/核心的电源策略：  
```bash
echo performance | sudo tee $i # $i为cpu线程/核心的编号
```

### CPU运行频率的更改

使用如下命令更改CPU频率上下限：  
```bash
cpufreq-set -c $i -d 4.50GHz -u 4.94GHz
```

### 永久生效

如果想要永久生效，必须手动写一个systemctl service或者将命令写入 `/etc/rc.local` ,并启用rc.local服务。通常情况下，还必须手写一个`rc.local.service`。（所以可以直接写一个单独的service）  

rc.local.service  
```yaml
[Unit]
Description=Run /etc/rc.local at startup
After=network.target

[Service]
Type=forking
ExecStart=/etc/rc.local start
TimeoutSec=0
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

rc.local  
```yaml
#!/bin/sh
for i in /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor; do
    echo performance | sudo tee $i > /dev/null;
done
for i in $(seq 0 15);do
    cpufreq-set -c $i -d 4.50GHz -u 4.94GHz
done
exit 0 # 必须以exit 0 结束
```

此外，记得给 `rc.local` 加可执行权限  
```bash
sudo chmod +x /etc/rc.local
```

### 其他问题

笔者使用的是AMD CPU，在笔者试图调整频率时发现不论是什么策略，可用频率都是离散的且最高频率并没有达到物理限制。最初的输出如下：  
```yaml
analyzing CPU 15:
  driver: acpi-cpufreq
  CPUs which run at the same hardware frequency: 15
  CPUs which need to have their frequency coordinated by software: 15
  maximum transition latency: 4294.55 ms.
  hardware limits: 1.60 GHz - 4.93 GHz
  available frequency steps: 3.30 GHz, 1.80 GHz, 1.60 GHz
  available cpufreq governors: powersave, conservative, userspace, ondemand, performance, schedutil
  current policy: frequency should be within 1.60 GHz and 3.30 GHz.
                  The governor "ondemand" may decide which speed to use
                  within this range.
```

在折腾一番后发现，电源的管理策略并不是amd的amd_pstate，而是一个名为`acpi-cpufreq`的设备在调控CPU运行频率。而且笔者在卸载这个调控设备后也无法加载且找不到pstate的调控设备。在笔者电脑的BIOS已经开启pstate支持下，问题显然在系统。通过`uname -r`笔者发现系统内核是6.1，而检索表明，Linux内核在6.1仅支持被动`passive`的pstate，只有在6.4及以上才支持`active`模式的pstate。那么，只需要更新内核、在grub中写明amd_pstate的模式即可。  

更新内核：  
```bash
sudo apt update
sudo apt install -t bookworm-backports linux-image-amd64
```

更改grub文件：  
```bash
sudo vim /etc/default/grub
```  
修改以下行  
```bash
GRUB_CMDLINE_LINUX_DEFAULT="quiet amd_pstate=active"
```
更新grub配置并重新启动：  
```bash
sudo update-grub
sudo reboot
```

此时再使用 `cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_driver` 查看当前的CPU频率调节驱动。  