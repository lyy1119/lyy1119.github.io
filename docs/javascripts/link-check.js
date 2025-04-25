document.addEventListener("DOMContentLoaded", function () {
    const skipList = [
        // "https://github.com/",
        "localhost",
        "wiki.lyy19.cn",
        // "beian.miit.gov.cn", // 备案
        // "beian.mps.gov.cn"
        // 可以继续加
    ];

    const links = document.querySelectorAll("a[href^='http']");

    links.forEach(link => {
        const url = link.href;

        // 跳过过滤列表中的链接
        if (skipList.some(skip => url.includes(skip))) {
            return;
        }

        // 创建状态标记
        const status = document.createElement("span");
        status.textContent = " ⏳";
        status.style.fontSize = "0.9em";
        link.parentNode.insertBefore(status, link.nextSibling);

        // 执行请求
        fetch(url, { method: "HEAD", mode: "no-cors" })
            .then(() => {
                status.textContent = " ✅";
            })
            .catch(() => {
                status.textContent = " ⛔";
                status.style.color = "red";
            });
    });
});

