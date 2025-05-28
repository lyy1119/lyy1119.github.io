# 在vscode中使用msys2 bash（Windows下）

`ctrl`+`shift`+`p`，去掉`>`，搜索并打开`settings.json`，用户目录下的那个。  

在`"terminal.integrated.profiles.windows"`键下加入如下内容：

```json
"bash msys2": {
            "path": [
                "C:\\msys64\\usr\\bin\\bash.exe"
            ],
            "args": [ //（json不允许注释，请在写入配置前删除） 此处不能用右边这个参数，会导致不能使用Windows下的git等软件 ："--login" , "-i",
                     "-c", "cd '${workspaceFolder}' && exec bash"
            ],
            "icon": "terminal-cmd"
        },
```

`ctrl` + `shift` + `p`,搜索并打开设置，搜索 `terminal integrated Windows` ，将默认终端改成上述键值。