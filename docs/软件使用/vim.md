# Vim使用教程

## vim配置

windows MSYS2的vim默认配置文件在`/usr/share/vim/vim91/defaults.vim`。  

根据自身习惯，罗列的常用快捷键等。  

Vim的模式： `NORMAL`、`INSERT`、`REPALCE`、`VISUAL`  

- 回到`NORMAL`： `Esc`

## NORMAL

- 进入`INSERT`： `a`或者`i`
- 进入`REPLACE`： `r`
- 进入`VISUAL`： `v`
- 写入： `:w`
- 退出： `:q`
- 写入并退出： `:wq`
- 跳转到行末： `$`
- 跳转到行首（第一个非空字符）： `^`
- 跳转到行首：`0`
- 跳转到指定行： `:行号` (如`:23`)
- 跳转到文件起始位置： `gg`
- 跳转到文末： `G`
- 撤销更改： `u`
- 复制整行： `yy`
- 粘贴： `p`
- 删除整行： `dd`
- 剪切整行（vim内）： `xx`
- 逐个字符删除：`x`
- 逐个字符delete： `<delete>` (也就是delete键)
- 复制到系统剪切板： `"+y` （需要安装clipboard拓展，下同）
- 从系统剪切板粘贴： `"+p`
- 查找特定值（如查找print）： `/print`
- 在查找模式下向下或者向上查找下一个： `n`或`N`

## VISUAL

部分NORMAL下的快捷键在VISUAL下也能使用，如删除、剪切、移动光标等。  

- 选中行整体缩进： `>`
- 选中行整体取消缩进： `<`
- 将a行到b行都缩进或取消缩进： `:a,b>` `:a,b<`

## Vim 拓展功能安装

```bash
sudo apt install vim-gtk3
```