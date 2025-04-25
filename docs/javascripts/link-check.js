document.addEventListener("DOMContentLoaded", function () {
    const skipList = [
        "localhost",
        "wiki.lyy19.cn",
    ];

    const links = document.querySelectorAll("a[href^='http']");

    links.forEach(link => {
        const url = link.href;

        // 跳过过滤的链接
        if (skipList.some(skip => url.includes(skip))) {
            return;
        }

        // 创建状态图标
        const status = document.createElement("span");
        status.className = "link-status";
        status.title = "检测中...";
        status.textContent = " ⏳";
        link.parentNode.insertBefore(status, link.nextSibling);

        // 请求
        fetch(url, { method: "HEAD", mode: "no-cors" })
            .then(() => {
                // status.textContent = " 🟢";
                status.textContent = "✅";
                status.title = "链接可访问";
            })
            .catch(() => {
                // status.textContent = " 🔴";
                status.textContent = "⛔";
                status.title = "链接无法访问";
                status.style.color = "red";
            });
    });
});

