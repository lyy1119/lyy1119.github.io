# 修改过去的commit

## 问题情景

当我们发现在过去的某个commit上出现代码错误（各种），我们希望做修改，但是为了commit信息的有序，我们又不希望继续在Head后修改，这时可以使用`git rebase`对某个commit做修改。  

!!! warning
    注意，对某个commit的修改不能影响到后续的commit。比如某行代码上某个变量名写错了，但是在未来的commit中，这行代码没有任何修改，那么你可以使用`git rebase`回去修改。  

    但是，如果你删除了过去commit中的某行，导致行号变化等问题，可能影响后续commit记录发挥正常作用，这个时候就不能使用`git rebase`修改。

## 步骤

### 1.查看git log

使用下述命令查看commit的简要信息。并确定你要修改的commit距离HEAD有几个commit。  
```bash
git log --oneline
```

### git rebase

如果要修改的commit为HEAD的上一个，就`git rebase -i HEAD~2`。  

如果要修改的commit与HEAD之间有`n`个commit，则命令为：  
```bash
git rebase -i HEAD~a # a = n+2
```

执行`rebase`命令后，你会进入一个文件，这是一些命令，将你要修改的commit前的`pick` 修改为 `edit`。  

```bash
edit abc123 Fix typo in readme
pick def456 Add new feature
pick ghi789 Update docs
```

### 修改文件

现在，你可以在你要修改的commit处的文件进行修改，修改完成后，`add`文件，然后`commit`，如下：  

```bash
git add <file>
git commit --amend
```

### 结束修改

```bash
git rebase --continue
```

此时，你的本地git仓库就完成了修改。如果之前没有`push`到远程仓库，直接`push`就行。如果之前已经push到了远程仓库，若有多人协作，必须在与他人沟通的情况下，强制`push`：  

```bash
git push --force-with-lease
```