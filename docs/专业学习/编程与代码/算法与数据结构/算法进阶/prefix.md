# 前缀和算法

前缀和算法顾名思义，就是将一个数组更新为前n个的和。  

前缀和（Prefix Sum）是一种非常实用的算法技巧，广泛应用于各种计算问题中，特别是在需要高效处理区间查询或区间统计的场景。以下是前缀和常见的应用场景和相关算法问题：


## **1. 区间和查询（Range Sum Queries）**
**问题类型**：给定一个数组，多次查询某个区间 `[L, R]` 的和。  
**暴力解法**：每次查询遍历 `L` 到 `R`，时间复杂度 `O(N)` 每次查询。  
**前缀和解法**：  

- 预处理前缀和数组 `prefix`，其中 `prefix[i] = arr[0] + arr[1] + ... + arr[i-1]`。
- 查询 `[L, R]` 的和 = `prefix[R+1] - prefix[L]`，时间复杂度 `O(1)` 每次查询。

**典型问题**：  

- [LeetCode 303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)
- [LeetCode 304. Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/)（二维前缀和）


## **2. 区间更新 + 单点查询（差分数组）**
**问题类型**：多次对数组的某个区间 `[L, R]` 进行增减操作，最后查询某个位置的值。  
**暴力解法**：每次更新遍历 `L` 到 `R`，时间复杂度 `O(N)` 每次更新。  
**差分数组解法**：  

- 使用差分数组 `diff`，其中 `diff[i] = arr[i] - arr[i-1]`。
- 区间 `[L, R]` 增加 `val`：`diff[L] += val`，`diff[R+1] -= val`。
- 最后计算前缀和还原数组，时间复杂度 `O(1)` 每次更新，`O(N)` 最终计算。

**典型问题**：  

- [LeetCode 1109. Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/)
- [LeetCode 370. Range Addition](https://leetcode.com/problems/range-addition/)


## **3. 统计区间覆盖次数**
**问题类型**：给定多个区间 `[L_i, R_i]`，统计每个点被多少个区间覆盖。  
**暴力解法**：遍历所有区间，逐个标记覆盖的点，时间复杂度 `O(M*N)`（`M` 是区间数，`N` 是点数）。  
**差分数组解法**：  

- 初始化 `diff` 数组，`diff[L_i]++`，`diff[R_i+1]--`。
- 计算前缀和得到每个点的覆盖次数，时间复杂度 `O(M + N)`。

**典型问题**：  

- AtCoder 城堡城墙问题
- [LeetCode 253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)（类似思想）


## **4. 滑动窗口优化（固定窗口求和）**
**问题类型**：在数组中寻找固定长度的子数组，使其满足某些条件（如和最大/最小）。  
**暴力解法**：遍历所有可能的窗口，计算和，时间复杂度 `O(N*K)`（`K` 是窗口大小）。  
**前缀和解法**：  

- 预处理前缀和数组 `prefix`。
- 计算窗口 `[i, i+K-1]` 的和 = `prefix[i+K] - prefix[i]`，时间复杂度 `O(N)`。

**典型问题**：  

- [LeetCode 643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)
- [LeetCode 209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

---

## **5. 矩阵区域和（二维前缀和）**
**问题类型**：给定二维矩阵，多次查询子矩阵的和。  
**暴力解法**：每次查询遍历子矩阵，时间复杂度 `O(M*N)` 每次查询。  
**二维前缀和解法**：  

- 预处理 `prefix[i][j]` 表示从 `(0,0)` 到 `(i-1,j-1)` 的和。
- 查询 `(x1,y1)` 到 `(x2,y2)` 的和：
  ```
  sum = prefix[x2+1][y2+1] - prefix[x1][y2+1] - prefix[x2+1][y1] + prefix[x1][y1]
  ```
  时间复杂度 `O(1)` 每次查询。

**典型问题**：  

- [LeetCode 304. Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/)
- [LeetCode 1314. Matrix Block Sum](https://leetcode.com/problems/matrix-block-sum/)

---

## **6. 统计满足条件的子数组个数**
**问题类型**：统计数组中满足某种条件的子数组个数（如和等于 `K`）。  
**暴力解法**：枚举所有子数组，时间复杂度 `O(N^2)`。  
**前缀和 + 哈希表优化**：  

- 维护前缀和 `prefix` 和哈希表 `count` 记录前缀和出现次数。
- 对于每个 `prefix[i]`，检查 `prefix[i] - K` 是否在 `count` 中，时间复杂度 `O(N)`。

**典型问题**：  

- [LeetCode 560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
- [LeetCode 1248. Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/)

---

## **7. 环形数组问题**
**问题类型**：在环形数组中计算某些区间性质（如最大子数组和）。  
**暴力解法**：拆分成线性情况，时间复杂度 `O(N^2)`。  
**前缀和解法**：  

- 计算前缀和，结合取模运算处理环形情况。

**典型问题**：  

- [LeetCode 918. Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/)

---

## **总结**
| 问题类型 | 暴力解法 | 前缀和解法 | 典型例题 |
|----------|---------|------------|----------|
| 区间和查询 | `O(N)` 每次查询 | `O(1)` 每次查询 | [LeetCode 303](https://leetcode.com/problems/range-sum-query-immutable/) |
| 区间更新 + 单点查询 | `O(N)` 每次更新 | `O(1)` 每次更新 | [LeetCode 370](https://leetcode.com/problems/range-addition/) |
| 区间覆盖统计 | `O(M*N)` | `O(M + N)` | 本题（AtCoder 城堡城墙） |
| 滑动窗口优化 | `O(N*K)` | `O(N)` | [LeetCode 209](https://leetcode.com/problems/minimum-size-subarray-sum/) |
| 二维矩阵查询 | `O(M*N)` 每次查询 | `O(1)` 每次查询 | [LeetCode 304](https://leetcode.com/problems/range-sum-query-2d-immutable/) |
| 子数组统计 | `O(N^2)` | `O(N)` | [LeetCode 560](https://leetcode.com/problems/subarray-sum-equals-k/) |
| 环形数组问题 | `O(N^2)` | `O(N)` | [LeetCode 918](https://leetcode.com/problems/maximum-sum-circular-subarray/) |

前缀和的核心思想是 **预处理数据，用空间换时间**，适用于 **频繁查询区间信息** 或 **需要高效区间更新** 的问题。结合差分数组，可以进一步优化区间操作。