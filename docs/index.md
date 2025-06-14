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
.profile-card {
    background-color: var(--md-default-bg-color);
    border-radius: 15px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    padding: 2rem;
    margin: 2rem 0;
    display: flex;
    gap: 2rem;
    align-items: center;
    transition: transform 0.3s ease;
}

.profile-card:hover {
    transform: translateY(-5px);
}

.profile-avatar {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    border: 3px solid var(--md-primary-fg-color);
    object-fit: cover;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.profile-info {
    flex: 1;
}

.profile-name {
    margin: 0;
    color: var(--md-primary-fg-color);
    font-size: 1.8em;
}

.profile-motto {
    color: var(--md-typeset-color);
    font-style: italic;
    margin: 0.5rem 0;
}

.profile-links {
    margin-top: 1rem;
    display: flex;
    gap: 1rem;
}

.profile-link {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    color: var(--md-typeset-color);
    text-decoration: none;
    transition: color 0.3s ease;
}

.profile-link:hover {
    color: var(--md-accent-fg-color);
}

@media (max-width: 600px) {
    .profile-card {
        flex-direction: column;
        text-align: center;
    }
    
    .profile-links {
        justify-content: center;
    }
}
</style>

<div class="profile-card">
    <img src="https://raw.githubusercontent.com/lyy1119/Imgs/main/img/1709210261156.png" alt="Avatar" class="profile-avatar">
    <div class="profile-info">
        <h1 class="profile-name">LYY19</h1>
        <p class="profile-motto">Stay hungry, stay foolish</p>
        <div class="profile-links">
            <a href="https://github.com/lyy1119" target="_blank" class="profile-link">
                <i class="fab fa-github"></i>
                GitHub
            </a>
            <a href="mailto:me@lycarus.cn" class="profile-link">
                <i class="fas fa-envelope"></i>
                Email
            </a>
        </div>
    </div>
</div>

<script>
// 添加简单的交互效果
document.querySelector('.profile-card').addEventListener('click', function() {
    this.style.transform = 'scale(0.98)';
    setTimeout(() => {
        this.style.transform = '';
    }, 200);
});
</script>


## mkdocs使用方法

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## 关于这个网站

本网站使用github repository作为图床，如果图片加载失败，可能你的网络连接存在问题。  

本网站还在建设中，难免有不足和错误之处，欢迎指正并在issue中提出。  

## 你好，访客

如果你恰好进入了我的网站，并看到了这段文字，那么欢迎你。在这个网站里，记录了许多我自己总结的经验，希望它们能帮到你。  
