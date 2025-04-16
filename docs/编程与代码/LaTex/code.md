# Latex的一些用法

## 取消页码显示

### 全局
在文档的导言区（`\begin{document}` 之前）加入：
```latex
\pagestyle{empty}
```

### 当前页
如果只想取消当前页的页码（如标题页），在需要取消页码的页面内使用：
```latex
\thispagestyle{empty}
```

### 通过文档类选项取消页码
某些文档类（如 `article`、`report`）支持 `nofoot` 选项：
```latex
\documentclass[nofoot]{article} % 或其他文档类
```

### 注意事项
1. 如果文档使用了 `\maketitle`，标题页默认会调用 `\thispagestyle{plain}`，可能需要额外添加：
   ```latex
   \maketitle
   \thispagestyle{empty} % 确保标题页无页码
   ```
2. 对 `book` 类文档，`\frontmatter` 部分默认使用 `plain` 页眉样式，建议配合 `\pagestyle{empty}` 使用。

如果需要部分页面取消页码（如目录后恢复页码），可以组合使用 `\pagestyle` 和 `\thispagestyle`。