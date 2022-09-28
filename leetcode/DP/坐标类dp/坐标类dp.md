
## 什么是坐标类DP

坐标型dp一般就是给你一个矩阵，然后状态数组的两个维度就分别代表矩阵的两个方向的额坐标。这雷题目通常会包含矩阵matrix, 矩形rectangle, 路径path等关键词

dp[i][j] 表示的是坐标从起点走到当前(i,j)时的状态

一般用来处理，pathSum(max, min), pathCount, 是否能到达， maxArea等

* 注意和序列型dp区分，序列型为前i个位置里，第i个位置一定选的答案，比如LIS，前面的位置是可以跳过的subsequence, 我们这里坐标型不可以跳跃必须向前走

来源: 古城算法 https://www.youtube.com/watch?v=BxblkIz6TZc&list=PLbaIOC0vpjNW9f04lmGAwVC-856a6y5gw&index=8