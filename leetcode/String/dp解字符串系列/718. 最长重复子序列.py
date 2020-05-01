"""
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

示例 1:

输入:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出: 3
解释:
长度最长的公共子数组是 [3, 2, 1]。
"""

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if not A or not B:
            return 0

        dp = [[0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]
        res = 0

        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

                if dp[i][j] > res:
                    res = dp[i][j]
        return res

"""
https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/dong-tai-gui-hua-by-hai-gen/
本题和1143可以一起看，基本上来说是属于同一类题
本题的递推式是这样理解的

dp[i][j] 是从[0~i） 和[0~j) 两者的最长相同子序列有多长
递推的方法是 假如说前一个字符相同 A[i-1] == B[j-1], 那么dp[i][j]就等于上一个字符的最长子串 +1
所以就是  dp[i][j] = dp[i - 1][j - 1] + 1

然后因为我们要求的是最长重复子序列，它是一种，只要不对，立刻清0的模式，所以不能完全记录过去的所有状态
所以在这里，我们需要用一个变量去不断更新最大值
而不是单纯地返回 dp[-1][-1]
"""