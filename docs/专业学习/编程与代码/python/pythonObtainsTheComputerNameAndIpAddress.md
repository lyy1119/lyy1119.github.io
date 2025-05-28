# Python获取计算机名与IP

![Static Badge](https://img.shields.io/badge/ALL_Generated_By-OpenAI-red)  

在 Python 中，可以通过 `socket` 模块获取计算机名，代码如下：

```python
import socket

# 获取计算机名
hostname = socket.gethostname()

print(f"计算机名: {hostname}")
```

### Windows 和 Linux 均适用

1. **`socket.gethostname()`**：
   - 返回的是计算机的主机名。此方法在 Windows 和 Linux 系统中均适用。

2. 如果需要获取计算机的完整域名（FQDN）：
   ```python
   fqdn = socket.getfqdn()
   print(f"完整域名: {fqdn}")
   ```

3. **获取主机对应的 IP 地址**：
   ```python
   ip_address = socket.gethostbyname(hostname)
   print(f"IP 地址: {ip_address}")
   ```

### 注意
- 返回值取决于操作系统和网络配置。
- 如果获取到的是 `localhost` 或回环地址（如 `127.0.0.1`），可能需要检查网络设置。