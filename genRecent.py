import subprocess
import os
import json
from pathlib import Path
from datetime import datetime
from urllib.parse import quote

# ========== 配置区域 ==========
DOCS_DIR = Path('docs')            # 使用 Path 对象
OUTPUT_JSON = DOCS_DIR / 'data/recent_posts.json'
EXCLUDE_FILES = {'index.md', 'about.md'}
MAX_POSTS = 5
GIT_COMMIT_COUNT = 30
# ==============================

def decode_git_path(raw_path):
    """处理被双引号包裹的八进制转义路径"""
    # 步骤1：去除首尾双引号
    stripped = raw_path.strip('"')
    
    # 步骤2：处理混合编码的八进制转义（如 \347）
    try:
        decoded = bytes(stripped, 'ascii').decode('unicode_escape')
    except UnicodeDecodeError:
        decoded = stripped
    
    # 步骤3：处理可能的二次编码
    try:
        final = bytes(decoded, 'latin-1').decode('utf-8')
    except UnicodeDecodeError:
        final = decoded
    
    # 步骤4：替换git的特殊空格转义
    return final.replace('\\ ', ' ')

def get_git_files():
    """获取文件列表（增强编码处理）"""
    cmd = [
        'git',
        'log',
        '--pretty=format:%H',
        '--name-only',
        f'-n {GIT_COMMIT_COUNT}',
        '--diff-filter=AM',
        '--'
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    
    files = []
    current_commit = None
    for line in result.stdout.splitlines():
        if len(line) == 40:
            current_commit = line
        elif line:
            decoded_path = decode_git_path(line)
            if decoded_path.endswith('.md'):
                files.append( (decoded_path, current_commit) )
    
    return files

def process_file(docs_path, rel_path, commit_hash):
    """处理单个文件"""
    full_path = docs_path / rel_path
    
    # 跳过不存在文件
    if not full_path.exists():
        return None

    # 提取标题
    title = None
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('# '):
                    title = line[2:].strip()
                    break
    except UnicodeDecodeError:
        print(f"解码失败: {rel_path}")
        return None

    # 生成URL（兼容中文路径）
    url_path = str(rel_path.with_suffix('')).replace('\\', '/')
    url = '/' + quote(url_path) + '/'

    # 获取日期
    try:
        date_cmd = ['git', 'log', '-1', '--date=format:%Y-%m-%d', '--pretty=format:%cd', commit_hash, '--', str(full_path)]
        date_str = subprocess.check_output(date_cmd, text=True).strip()
        date_display = datetime.strptime(date_str, "%Y-%m-%d").strftime("%m/%d")
    except:
        date_display = "近期"

    return {
        'title': title or url_path.stem.replace('-', ' ').title(),
        'url': url,
        'date': date_display
    }

def main():
    docs_path = DOCS_DIR.resolve()
    seen = set()
    posts = []

    for git_path, commit_hash in get_git_files():
        # 转换为绝对路径
        try:
            abs_path = Path(git_path).resolve()
            rel_path = abs_path.relative_to(docs_path)
        except ValueError:
            continue  # 不在 docs 目录下的文件
        except Exception as e:
            print(f"路径解析错误: {git_path} - {e}")
            continue

        # 去重处理
        path_key = str(rel_path).lower()
        if path_key in seen:
            continue
        seen.add(path_key)

        # 排除文件
        if rel_path.name in EXCLUDE_FILES:
            continue

        # 处理文件
        if (post := process_file(docs_path, rel_path, commit_hash)):
            posts.append(post)
            if len(posts) >= MAX_POSTS:
                break

    # 写入 JSON
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)

    print(f"成功处理 {len(posts)} 篇文章，保存至 {OUTPUT_JSON}")

if __name__ == '__main__':
    main()