import subprocess
import os
import json
from collections import defaultdict

# 配置参数
DOCS_DIR = 'docs'  # MkDocs文档目录
OUTPUT_JSON = os.path.join(DOCS_DIR, 'data', 'recent_posts.json')  # 输出文件路径
EXCLUDE_FILES = ['index.md', 'about.md']  # 排除的非文章文件
MAX_POSTS = 5  # 最大显示数量

# 获取最近修改的.md文件（最多30次提交）
cmd = "git log --pretty=format:%H --name-only -n 30 | awk '/^$/{if (commit) {commit=0} else {commit=1}} commit==0 && /\.md$/{print}'"
output = subprocess.check_output(cmd, shell=True).decode('utf-8')

# 处理文件路径并按提交时间排序
files = defaultdict(list)
for line in reversed(output.splitlines()):
    filepath = line.strip()
    if filepath.endswith('.md') and os.path.exists(filepath):
        files[filepath].append(line)

# 去重并保留顺序
unique_files = []
seen = set()
for f in files:
    if f not in seen and os.path.dirname(f).startswith(DOCS_DIR):
        seen.add(f)
        unique_files.append(f)

# 过滤排除文件和生成数据
posts = []
for filepath in unique_files[:MAX_POSTS*2]:  # 获取更多以防过滤
    if os.path.basename(filepath) in EXCLUDE_FILES:
        continue
    
    # 提取标题
    title = None
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('# '):
                title = line[2:].strip()
                break
        if not title:  # 使用文件名作为标题
            title = os.path.splitext(os.path.basename(filepath))[0].replace('-', ' ').title()
    
    # 生成URL（假设use_directory_urls: true）
    url_path = os.path.splitext(filepath[len(DOCS_DIR)+1:])[0].replace('\\', '/')
    url = f'/{url_path}/'
    
    # 在 posts.append 部分增加日期获取：
    date_str = subprocess.check_output(
        f'git log -1 --pretty=format:%cd --date=format:"%Y-%m-%d" {filepath}',
        shell=True
    ).decode('utf-8').strip()

    posts.append({
        'title': title,
        'url': url,
        'date': date_str  # 添加日期字段
    })
    if len(posts) >= MAX_POSTS:
        break

# 写入JSON文件
os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(posts, f, indent=2)

print(f'Generated {OUTPUT_JSON} with {len(posts)} recent posts')