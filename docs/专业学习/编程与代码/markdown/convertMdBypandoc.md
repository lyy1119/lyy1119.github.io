# 使用pandoc转换md文件

## pandoc下载

[pandoc官网](https://pandoc.org/)

## markdown转化为doc/docx

- 通用命令

```bash
pandoc markdown.md -o document.docx
```

- 指定模板文件（读取docx里的标题、正文格式）

```bash
pandoc -s m.md --reference-doc custom-reference.docx -o m.docx
```

## markdown转换HTML5

```bash
pandoc -f markdown -t html5 input.md -o output.html
```

## Word转换为markdown

```bash
pandoc document.docx -o markdown.md
```