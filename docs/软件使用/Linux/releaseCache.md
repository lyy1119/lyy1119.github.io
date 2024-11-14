# 查看内存状态、手动释放缓存

## 查看内存状态

```bash
free -h
```

## 手动释放缓存

```bash
echo 3 > /proc/sys/vm/drop_caches
```