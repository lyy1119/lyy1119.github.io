# 我的makefile模板

边学边写中……  

```makefile
# CC设置
CC = gcc

# OS
OS := $(shell uname -s)

# RM
ifeq ($(OS),Linux)
    RM := rm -rf
else ifeq ($(OS),Darwin)
    RM := rm -rf
else ifneq (,$(findstring MSYS,$(OS)))
    RM := del /f /q  # MSYS2 uses Windows del
else ifneq (,$(findstring MINGW,$(OS)))
    RM := del /f /q  # MinGW uses Windows del
else ifneq (,$(findstring CYGWIN,$(OS)))
    RM := rm -rf  # Cygwin uses rm
else
    RM := echo "Unknown OS"
endif

default: compile .clean

compile:
    #  仅仅是示例
    $(CC) $(TARGET) $(OUT)

.clean:
    $(RM) file
```