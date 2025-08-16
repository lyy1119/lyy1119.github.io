# tail命令常用指南


## 1. 基本功能

`tail` 用于**查看文件的末尾部分**。默认显示文件最后 **10 行**。

```bash
tail filename
```


## 2. 常用选项

### **`-n`** 指定行数

```bash
tail -n 20 filename
```

显示文件最后 **20 行**。


### **`-n +N`** 从第 N 行开始

```bash
tail -n +100 filename
```

从第 **100 行**开始，显示到文件结尾。


### **`-f`** 实时跟踪

```bash
tail -f filename
```

显示文件末尾，并持续输出新内容。常用于**实时监控日志**。


### **`-n NUM -f`** 结合使用

```bash
tail -n 50 -f filename
```

先显示最后 **50 行**，再继续跟踪新增内容。


### **`-F`** 智能跟踪

```bash
tail -F filename
```

类似 `-f`，但能自动处理**日志轮转**（文件重命名或替换时仍会继续跟踪）。


## 3. 常见应用场景

### **(1) 查看日志文件末尾**

```bash
tail -n 100 /var/log/syslog
```

查看系统日志最后 100 行。


### **(2) 实时监控日志**

```bash
tail -f /var/log/nginx/access.log
```

实时查看 Nginx 访问日志。


### **(3) 结合 `grep` 过滤**

```bash
tail -f app.log | grep "ERROR"
```

只输出日志中包含 **ERROR** 的行。


### **(4) 实时统计**

```bash
tail -n 1000 access.log | wc -l
```

统计日志最后 1000 行的行数。


### **(5) 程序输入管道**

```bash
tail -f /tmp/input | java MyProgram
```

将文件内容实时传递给 Java 程序。

## 4. 使用技巧

* **只看最新写入**

  ```bash
  tail -n 0 -f file.log
  ```

  不显示历史内容，只从新写入的行开始看。

* **多个文件**

  ```bash
  tail -f file1.log file2.log
  ```

  同时监控多个文件。

* **和 `less` 结合**

  ```bash
  tail -n 1000 file.log | less
  ```

  分页查看文件最后 1000 行。

## 5. 小结

* `tail` 默认显示文件末尾 10 行。
* `-n` 控制行数，`+N` 表示从第 N 行开始。
* `-f` 用于实时跟踪文件变化，`-F` 更智能，适合日志轮转。
* 常与 `grep`、`wc`、`awk`、管道结合，用于日志分析、实时监控和数据处理。

