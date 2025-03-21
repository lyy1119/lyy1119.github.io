# 在msys2的bash中开启中文支持

同样适用于git bash。

```bash
echo 'export LANG=zh_CN.UTF-8' >> ~/.bashrc
echo 'export LC_ALL=zh_CN.UTF-8' >> ~/.bashrc
source ~/.bashrc

```