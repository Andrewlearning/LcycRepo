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

        # 初始化dp数组， dp[A用了几个字符][B用了几个字符]
        dp = [[0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]
        res = 0

        # 我们不用定义初始状态，因为dp[0][0]两个空字符串没有公共序列

        # 从两个字符串的第一个字符开始遍历
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                # 假如两个字符相等
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

                # 因为我们要求连续，所以不能像1143一样
                # 可以把最近的状态的最值保留住，而是dp[i][j]直接等于0

                # 不断更新结果
                if dp[i][j] > res:
                    res = dp[i][j]
        return res

"""
https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/dong-tai-gui-hua-by-hai-gen/
"""