# markdown图片居中及图片标题

在写markdown插入图片时使用如下html和css代码即可，使用css可以控制图片大小  

```html
<div align=center>  <!--使整体居中-->
    <div style="width: 50%;">			<!--块级封装-->
        <center>	<!--将图片和文字居中-->
        <img src="图片链接"
            alt="图片无法加载，请检查网络连接"/>
        <br>		<!--换行-->
        <div style="font-size: 12px;font-style:italic;">
            图片标题
        </div>	<!--标题-->
        </center>
    </div>
</div>
```