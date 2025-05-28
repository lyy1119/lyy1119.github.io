# D - Domino Covering XOR

[原题连接](https://atcoder.jp/contests/abc407/tasks/abc407_d)

## 思路

使用暴力搜索，穷举所有可能。  

对于一个任意大小、任意形状的网格，对于其中一个格子，可能有以下三种情况：  

1. 没有被多米诺骨牌占用
2. 被水平多米诺骨牌占用
3. 被竖直多米诺骨牌占用

可以使用掩码来表示整个网格的占用情况。使用`与`运算来判断当前格子能否放置水平或者竖直多米诺骨牌。  

```pytho title="Python"
h, w = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(h)]

mask = [0] # no cell covered initially

horizonMask = 3 # 11
verticalMask = (1 << w) + 1 # 1 \n 1


# all possible layout

bitPos = 0
for i in range(h): # lines
    for j in range(w): # rows
        tmp = []
        for k in mask:
            # can place in horizon
            if j + 1 < w and not(k & (horizonMask << bitPos)):
                # place
                tmp.append(k | (horizonMask << bitPos))
            # can place in vertical
            if i + 1 < h and not(k & (verticalMask << bitPos)):
                tmp.append(k | (verticalMask << bitPos))
            # move pos
        bitPos = bitPos + 1
        mask = mask + tmp

result = 0
for p in mask:
    # p stand for each placement
    tmp = 0
    bitPos = 0
    for i in range(h):
        for j in range(w):
            if ((1 << bitPos) & p)== 0:
                tmp = tmp^grid[i][j]
            bitPos += 1
    result = max(result, tmp)

print(result)

```