# 使用Velocity搭建群组服务器

| [Velocity](https://papermc.io/software/velocity) | [Proxy Compatible Forge](https://www.mcmod.cn/class/13564.html) | 

## 群组服务器能做什么

1. 统一多个服务器的登陆入口以提供身份验证等，如小游戏服的跳转。  
2. 对于物理设备少，但是性能足够的物理服务器，能整合端口
3. 对于生电等，可以做到生存服、创造服、镜像服的整合
4. 可以支持正版、离线同时在线
5. 对于仅有优化的模组包，甚至可以实现forge和fabric同时存在于同一服务器

## 不足

`Velocity`的本质就是代理。因此，所有流量必然经过`Velocity`，如果反向代理的子服务端与`Velocity`的延迟较大，或者玩家处于`Velocity`和子服务端的中间地带，那么反向代理的体验会很差。  

## Velocity介绍

`Velocity`是一个反向代理软件，如果你曾做过`nginx`相关的反向代理，如通过指定域名代理到指定服务，那么`Velocity`就很容易理解。  

`Velocity`并不是一个 **服务端** ，他只是一个流量代理软件，如果要实现大厅功能，需要服主自己创建一个大厅服务器`lobby`。这个服务器可以是任何版本、添加任何mod的服务端，只要玩家能正常进入即可。  

`Velocity`还支持插件，通过安装`MultiLogin-Velocity`插件，能实现官方正版和Littleskin第三方同时在线。  

## 搭建Velocity

[Velocity官方文档](https://docs.papermc.io/velocity/)  

建议有英语阅读能力的读者先去看官方文档和配置文件注释（配置文件及相关内容在官方文档中有提及）。  

### 下载`Velocity.jar`

这就不必多说了吧。  

### 运行`Velocity.jar`

运行命令如下：  
```bash
java -Xms512M -Xmx512M -XX:+UseG1GC -XX:G1HeapRegionSize=4M -XX:+UnlockExperimentalVMOptions -XX:+ParallelRefProcEnabled -XX:+AlwaysPreTouch -XX:MaxInlineLevel=15 -jar velocity.jar
```
!!! info
    上述命令相比较官方，将内存限制改为512MB。由于`Velocity`仅仅用于转发，所以在玩家不多的情况下，分配512MB到1G绰绰有余。

### 配置`Velocity.toml`

官方文档已经说明的足够详细，这里仅说明一些笔者自己在配置时所做的修改等。下文中没有展示的配置及注释表示笔者并没做什么修改，或者看官方文档已经足够。  

```toml
# Config version. Do not change this
config-version = "2.7"

# 绑定端口，0.0.0.0表示接受来自所有ip4地址的流量
bind = "0.0.0.0:25565"

# motd，即展示在server list下的文字，按自己喜好配置即可，可自行搜索相关语法等
motd = "<#09add3>A Velocity Server"

# 最大玩家数
show-max-players = 50

# 是否开启正版验证，注意，即使我们想使用littleskin支持离线玩家，也需要设置为true
online-mode = true

...

# 设置为modern即可，如果有特殊需求，参见官方注释
player-info-forwarding-mode = "modern"

...


[servers]
# 子服务端列表，等号左侧表示显示名称，等号右侧表示ip及端口号
# 如果名称要中文，则需要用英文双引号包围，如 "服务器" = ip:port
# 注意，服务器名称不能有"[ 、 ]"等可能引起命令行解析出错的符号
lobby = "mclobby-1-18:25565"
CAE = "mccae:25565"

# 默认尝试列表，当加入Velocity显示的服务器时，Velocity会按照下面的顺序尝试加入服务器
# try是一个list
try = [
    "lobby",
]

[forced-hosts]
# 强制转发，即根据连接服务器传递的host，在加入服务器时直接转发到对于服务器
# 需要设置域名解析到Velocity的ip
# 写法为
# "domain.com" = ["serverName"]
# serverName仅能为[servers]中的
"mcgame.lyy19.cn" = [ "CAE" ]

...

```

### 什么是`secret`

在`Velocity`根目录下有这个文件`forwarding.secret`。这个文件存的字符串就是转发的`secret`，或者说密钥。  

### 配置插件

将插件下载放入`Velocity`的`plugins`文件夹下即可，这里推荐几个mod：  

1. 离线登陆支持：[MultiLogin-Velocity](https://github.com/CaaMoe/MultiLogin)
2. forge服务端支持：[Ambassador](https://modrinth.com/plugin/ambassador) （forge服务端需要安装[Proxy Compatible Forge](https://www.mcmod.cn/class/13564.html)）  
3. 跨版本支持：[ViaVersion](https://www.mcmod.cn/class/5760.html)，*“既是`Velocity`插件，又是`paper`插件，又是`sponge`插件，还是`bc`、`waterfall`，还是`fabric`模组”*

#### MutiLogin配置

在放入`plugins`文件夹下，重启`Velocity`后，会在`plugins`下看到`multilogin`文件夹，根据官方[wiki](https://github.com/CaaMoe/MultiLogin/wiki#%E7%AE%80%E5%8D%95%E9%85%8D%E7%BD%AE)，这里将`examples`下的`official.yml`和`littleskin.yml`复制到`services`下，同时修改两个文件中的`id`，让两个id不同即可。  

## forge服务端支持

默认只有`Velocity`团队开发的`paper`服务端原生支持`modern`转发，对于已有的forge服务端，可以通过在`Velocity`安装`Ambassador`，在服务端安装`Proxy Compatible Forge`实现。  

在服务端安装`Proxy Compatible Forge`后，重启服务器，能看到`config`文件夹下多了一个`pcf-common.toml`的文件，编辑这个文件，将`Velocity`的`secret`填入`forwardingSecret=`后，重启即可。  

!!! warning
    如果`Velocity`开启了正版验证，那么子服务端必须关闭，因为流量是从`Velocity`转发来的，包括正版验证的uuid等数据，所以子服务端也没必要且不能开启正版验证。  

## Paper服务端的原生支持

从这个[网站](https://gist.github.com/osipxd/6119732e30059241c2192c4a8d2218d9)的链接可以下载旧版paper服务端。  

运行一次paper服务端核心后，可以在服务端根目录下发现`paper.yml`这个文件。  

在`paper.yml`中，配置如下几行可支持`modern`转发：  
```yml
  velocity-support:
    enabled: true
    online-mode: true
    secret: xaLoxnaTv
```