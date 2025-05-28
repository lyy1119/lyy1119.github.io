# Debian安装软件时提示插入光盘

## 问题原因

Debian安装好后，默认使用光盘做apt源。  

## 解决方案

编辑`/etc/apt/sources.list`，将使用光盘做源的那一行注释掉即可。