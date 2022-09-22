## 什么是双序列型动态规划

双序列顾名思义就是给你`两个序列`放一块问你怎么做。一般有两个数组或两个字符串，计算其匹配关系。双序列中常用二维数组表示状态转移关系，但往往可以使用滚动数组对空间复杂度进行优化

* state: dp[i][j] 表示了第一个sequence的前i个数字/字符，配上第二个sequence的前j个数字/字符所能表示的状态
* 可以是Longest common subsequence, 也可以是minimal edi distance
* 常常和string一起出现，number的情况也不少，一般为二维dp

考察概率为30%

https://www.youtube.com/watch?v=bPDAhMU_Sqg