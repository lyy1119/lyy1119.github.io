# 欢迎

这是一个使用mkdocs搭建的wiki，mkdocs官方文档见： [mkdocs.org](https://www.mkdocs.org)  

## 📖 最近更新

<!-- 最近更新占位符 -->
<div id="recent-posts-container">
  <div class="loading-spinner" style="display: none;"></div>
  <ul id="recent-posts-list"></ul>
</div>
<script>
// 改进版本：包含完整的加载状态管理
const recentPosts = {
  container: null,
  list: null,
  spinner: null,

  init() {
    this.container = document.getElementById('recent-posts-container');
    this.list = document.getElementById('recent-posts-list');
    this.spinner = document.querySelector('.loading-spinner');
    
    if (!this.container) return;

    this.showLoading();
    this.loadPosts()
      .finally(() => this.hideLoading());
  },

  showLoading() {
    if (this.spinner) {
      this.spinner.style.display = 'inline-block';
    }
    if (this.list) {
      this.list.innerHTML = '';
    }
  },

  hideLoading() {
    if (this.spinner) {
      this.spinner.style.display = 'none';
    }
  },

  async loadPosts() {
    try {
      const response = await fetch('/data/recent_posts.json?_=' + Date.now());
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const posts = await response.json();
      this.render(posts);
      
    } catch (error) {
      console.error('Recent posts load failed:', error);
      this.showError('暂时无法加载最新文章');
    }
  },

  render(posts) {
    if (!this.list) return;
    
    if (posts.length === 0) {
      this.list.innerHTML = '<li class="empty">暂无最近更新</li>';
      return;
    }

    this.list.innerHTML = posts.slice(0, 5).map(post => `
      <li class="post-item">
        <a href="${post.url}" class="post-link">
          ${post.title}
          <span class="post-date">${post.date}</span>
        </a>
      </li>
    `).join('');
  },

  showError(message) {
    if (this.list) {
      this.list.innerHTML = `<li class="error">${message}</li>`;
    }
  }
};

// 初始化（带防抖处理）
let initialized = false;
document.addEventListener('DOMContentLoaded', () => {
  if (!initialized) {
    recentPosts.init();
    initialized = true;
  }
});
</script>

<style>
/* 改进后的加载动画 */
.loading-spinner {
  display: none; /* 默认隐藏 */
  width: 24px;
  height: 24px;
  margin: 8px 0;
  border: 3px solid rgba(0,0,0,0.1);
  border-radius: 50%;
  border-top-color: #007bff;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* 其他样式保持不变... */
</style>

## 关于我

<style>
    .parent {
    width: 80%;
    display: grid;
    grid-template-columns: 6fr 2fr 3fr;
    grid-template-rows: repeat(4, 1fr);
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    border-color:#4FC9F1;
    border-style:inset;
    border-width:5px;
    border-radius: 5% 5% 5% 5% / 10% 10% 10% 10%;
    padding: 1em;
    min-width: 25em;
    }

    .div1 { grid-area: 1 / 1 / 5 / 2; padding: 5px;min-width: 10em;margin: -0.5em 1em 0 auto;}
    .div2 { grid-area: 1 / 2 / 5 / 4; }
    .div3 { grid-area: 1 / 2 / 2 / 3; min-width: 7em;}
    .div4 { grid-area: 1 / 3 / 2 / 4; padding-left: 10px;}
    .div5 { grid-area: 2 / 2 / 3 / 3; }
    .div6 { grid-area: 2 / 3 / 3 / 4; padding-left: 10px;}
    .div7 { grid-area: 3 / 2 / 4 / 3; }
    .div8 { grid-area: 3 / 3 / 4 / 4; padding-left: 10px;}
    .div9 { grid-area: 4 / 2 / 5 / 3; }
    .div10 { grid-area: 4 / 3 / 5 / 4; padding-left: 10px;}
</style>

<div class="parent">

<div class="div1">
    <img align=center style="border-radius: 5% 5% 5% 5%;" src="https://raw.githubusercontent.com/lyy1119/Imgs/main/img/1709210261156.png" alt="来自github的图片加载失败，请检查网络"></div>

<div class="div2"></div>

<div class="div3"><img align=center src=https://img.shields.io/badge/Github-Profile-blue></div>

<div class="div4"><a href="https://github.com/lyy1119">lyy1119</a></div>

<div class="div5"><img align=center src="https://img.shields.io/badge/email-red"></div>

<div class="div6">lyy2286301015@126.com</div>

<div class="div7"><img align=center src=https://img.shields.io/badge/wiki-blue></div>
<div class="div8"><a href="https://exp.lyy19.top/">wiki.lyy19.cn</a></div>
<div class="div9"><img align=center src=https://img.shields.io/badge/wiki-githubpages-blue></div>
<div class="div10"><a href="https://lyy1119.github.io/">lyy1119.github.io</a></div>
</div>

## mkdocs使用方法

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## 关于这个网站

创建这个网站的主要目的不是去像博客那样分享。主要目的是记录自己的经验。为什么不用虚拟内网建站？主要考虑到在一些未并网设备上查阅的方便，并且，经验也没有必要像文件和资料那样具有安全性的要求。  

本网站使用github repository作为图床，如果图片加载失败，可能你的网络连接存在问题。  

本网站 **部分内容使用ai生成** 并经过审核，对于ai生成的文字内容，将在标题打上形如 ![Static Badge](https://img.shields.io/badge/Generated_By-OpenAI-red) 的徽章。  

本网站还在建设中，难免有不足和错误之处，欢迎指正并在issue中提出。  

## 你好，访客

如果你恰好进入了我的网站，并看到了这段文字，那么欢迎你。在这个网站里，记录了许多我自己总结的经验，希望它们能帮到你。  