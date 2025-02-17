---
comments: true  #默认不开启评论
description: "欢迎来看我的摄影照片，如果你喜欢它，请给我一个👍或❤。"
---
# 摄影展

点击图片可查看原图  
如果你喜欢它，请给我一个👍或❤。  
使用桌面端获得更好浏览体验。

## 2024-12

### 北京·雍和宫
<div class="gallery" id="2024121"></div>

## 2025-1
### 南京·明孝陵

<div class="gallery" id="2025011"></div>

<!-- real image div, style and js-->
<!-- 模态框：点击缩略图显示原图 -->
<div class="modal" id="modal">
    <div>
        <img id="modal-img" src="" alt="">
        <div class="caption" id="modal-caption"></div>
    </div>
</div>
<style>
/* 图册使用 flex 布局 */
.gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    gap: 10px;
}
.photo-item {
    flex: 1 1 calc(33.33% - 10px);
    max-width: calc(33.33% - 10px);
    margin-bottom: 20px;
    text-align: center;
}
@media (max-width: 768px) {
    .photo-item {
        flex: 1 1 calc(50% - 10px);
        max-width: calc(50% - 10px);
    }
}
@media (max-width: 480px) {
    .photo-item {
        flex: 1 1 100%;
        max-width: 100%;
    }
}
/* 缩略图容器，保证统一尺寸（此处使用 4:3 长宽比，可根据需求调整） */
.thumb-container {
    position: relative;
    aspect-ratio: 4 / 3;
    width: 100%;
    overflow: hidden;
}
/* 高斯模糊背景层 */
.thumb-container .bg {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
    filter: blur(8px);
    transform: scale(1.1);
}
/* 前景图片，保持原图长宽比并居中显示 */
.thumb-container img {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    max-width: 90%;
    max-height: 90%;
    object-fit: contain;
    border: 5px solid #fff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
.caption {
    margin-top: 8px;
    font-size: 14px;
    color: #333;
}
/* 模态框样式（点击缩略图显示原图） */
.modal {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    align-items: center;
    justify-content: center;
}
.modal img {
    max-width: 90%;
    max-height: 80vh;
    border: 5px solid #fff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
.modal .caption {
    color: #fff;
    margin-top: 10px;
    text-align: center;
}
</style>
<script>
    // 定义图片数据：缩略图、原图链接和图题
    var images = [
        // 北京 雍和宫
        {
            pos: "2024121",
            img: [
                { thumb: "https://raw.githubusercontent.com/lyy1119/Imgs/main/img/DSC_5052.webp", full: "https://raw.githubusercontent.com/lyy1119/Imgs/main/img/DSC_5052.jpg", title: "雍和门"},
                { thumb: "https://raw.githubusercontent.com/lyy1119/Imgs/main/img/DSC_5056.webp", full: "https://raw.githubusercontent.com/lyy1119/Imgs/main/img/DSC_5056.jpg", title: "雍和宫牌匾"},
                { thumb: "https://raw.githubusercontent.com/lyy1119/Imgs/main/img/DSC_5063%7E1.webp", full: "https://raw.githubusercontent.com/lyy1119/Imgs/main/img/DSC_5063.jpg", title: "雍和宫一角 1"},
                { thumb: "https://raw.githubusercontent.com/lyy1119/Imgs/main/img/DSC_5066%7E1.webp", full: "https://raw.githubusercontent.com/lyy1119/Imgs/main/img/yonghegong.jpg", title: "雍和宫一角 2"},
            ]
        },
        // 南京明孝陵
        {
            pos: "2025011",
            img: [
                { thumb: "https://raw.githubusercontent.com/lyy1119/Imgs/main/img/明孝陵-4.webp", full: "https://raw.githubusercontent.com/lyy1119/Imgs/main/img/明孝陵-4.jpg", title: "明孝陵红墙的一角"},
                { thumb: "https://raw.githubusercontent.com/lyy1119/Imgs/main/img/明孝陵-1.webp", full: "https://raw.githubusercontent.com/lyy1119/Imgs/main/img/明孝陵-1.jpg", title: "林间小路"},
                { thumb: "https://raw.githubusercontent.com/lyy1119/Imgs/main/img/明孝陵-3.webp", full: "https://raw.githubusercontent.com/lyy1119/Imgs/main/img/明孝陵-3.jpg", title: "屋顶腊梅"},
                { thumb: "https://raw.githubusercontent.com/lyy1119/Imgs/main/img/明孝陵-5.webp", full: "https://raw.githubusercontent.com/lyy1119/Imgs/main/img/明孝陵-5.jpg", title: "红墙腊梅 1"},
                { thumb: "https://raw.githubusercontent.com/lyy1119/Imgs/main/img/thumb4.jpg.webp", full: "https://raw.githubusercontent.com/lyy1119/Imgs/main/img/明孝陵-7.jpg", title: "红墙腊梅 2"},
                { thumb: "https://raw.githubusercontent.com/lyy1119/Imgs/main/img/明孝陵-9.webp", full: "https://raw.githubusercontent.com/lyy1119/Imgs/main/img/明孝陵-9.jpg", title: "梅花鹿"},
            ]
        },
        // template
        // {
            // pos: "",
            // img: [
                // { thumb: "thumb4.jpg", full: "full4.jpg", title: "城市夜景" },
                // { thumb: "thumb5.jpg", full: "full5.jpg", title: "山间小路" }
            // ]
        // }
    ];
    var modal = document.getElementById("modal");
    var modalImg = document.getElementById("modal-img");
    var modalCaption = document.getElementById("modal-caption");
    // 载入所有图片及图题
    images.forEach(function (images) {
        var gallery = document.getElementById(images.pos);
        images.img.forEach(function (img)
            {
                // 创建图片项容器
                var itemDiv = document.createElement("div");
                itemDiv.className = "photo-item";
                // 创建缩略图容器
                var thumbContainer = document.createElement("div");
                thumbContainer.className = "thumb-container";
                thumbContainer.onclick = function () {
                    modal.style.display = "flex";
                    modalImg.src = img.full;
                    modalCaption.textContent = img.title;
                };
                // 创建高斯模糊背景层
                var bgDiv = document.createElement("div");
                bgDiv.className = "bg";
                bgDiv.style.backgroundImage = "url(" + img.thumb + ")";
                // 创建前景图片
                var imageElement = document.createElement("img");
                imageElement.src = img.thumb;
                imageElement.alt = img.title;
                // 将背景层和前景图片添加到缩略图容器
                thumbContainer.appendChild(bgDiv);
                thumbContainer.appendChild(imageElement);
                // 创建图题元素
                var captionDiv = document.createElement("div");
                captionDiv.className = "caption";
                captionDiv.textContent = img.title;
                // 组合图片项
                itemDiv.appendChild(thumbContainer);
                itemDiv.appendChild(captionDiv);
                gallery.appendChild(itemDiv);
            }
        );
    });
    // 点击模态框任意位置关闭
    modal.onclick = function () {
        modal.style.display = "none";
    };
</script>