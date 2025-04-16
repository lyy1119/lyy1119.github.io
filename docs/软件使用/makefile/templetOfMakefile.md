# 我的makefile模板

边学边写中……  

```makefile
# CC设置
CC = gcc
TRAGE = # output file full name
ARGS = # input parameters here
TEMP = # temp files need to be deleted

# OS
OS := $(shell uname -s)

# RM
ifeq ($(OS),Linux)
    RM := rm -rf
else ifeq ($(OS),Darwin)
    RM := rm -rf
else ifneq (,$(findstring MSYS,$(OS)))
    RM := rm -rf # MSYS2 uses rm
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
    $(CC) $(ARGS) $(TARGET) $(OUT)

.clean:
    $(RM) $(TEMP)

clean:
    $(RM) $(TARGET)
```