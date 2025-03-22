# Linux或bash光标消失

使用`echo`就能解决。  

显示光标  
```bash
echo -e "\033[?25h"
```

隐藏光标
```python
echo -e "\033[?25l"
```