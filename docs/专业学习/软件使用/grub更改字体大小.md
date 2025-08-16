# 如何更改 GRUB 字体及大小

GRUB 默认使用的字体较小，如果觉得看不清楚，可以通过以下方法更换字体并调整大小。方法核心是 **将 TTF 字体转换为 GRUB 支持的 `.pf2` 格式**，并在配置文件中启用。


## 一、准备工具

1. **安装 `grub-mkfont` 工具**（用于生成 `.pf2` 字体文件）：

   * Debian/Ubuntu：

     ```bash
     sudo apt install grub2-common
     ```
   * Arch Linux：

     ```bash
     sudo pacman -S grub
     ```

2. **确认字体文件路径**
   常见字体路径：

   * `/usr/share/fonts/truetype/`
   * `~/.local/share/fonts/`


## 二、生成 `.pf2` 字体文件

使用 `grub-mkfont` 指定字体大小并输出为 `.pf2`：

```bash
sudo grub-mkfont -s 32 -o /boot/grub/fonts/myfont.pf2 /usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf
```

参数说明：

* `-s 32` → 字体大小（数值越大字体越大，常见范围 24\~48）
* `-o` → 输出文件路径
* 最后跟 `.ttf` 文件路径

你可以尝试多生成几份不同大小的 `.pf2` 文件，方便切换。


## 三、修改 GRUB 配置

编辑配置文件：

```bash
sudo nano /etc/default/grub
```

添加或修改以下行：

```bash
GRUB_FONT=/boot/grub/fonts/myfont.pf2
```

确保路径和你的 `.pf2` 文件一致。


## 四、更新 GRUB 配置

更新命令因系统而异：

* BIOS/Legacy 系统：

  ```bash
  sudo grub-mkconfig -o /boot/grub/grub.cfg
  ```

* UEFI 系统：

  ```bash
  sudo grub-mkconfig -o /boot/efi/EFI/$(ls /boot/efi/EFI | head -n 1)/grub.cfg
  ```

（如果不确定，可以 `find /boot -name grub.cfg` 查找实际路径）


## 五、重启查看效果

重启后，你会看到 GRUB 界面使用了新的字体大小。
