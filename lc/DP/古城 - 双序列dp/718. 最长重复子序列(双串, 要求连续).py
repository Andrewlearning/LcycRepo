"""
给两个整数数组 nums1 和 nums2 ，返回两个数组中公共的、长度最长的子数组的长度。

示例 1:

输入:
nums1: [1,2,3,2,1]
nums2: [3,2,1,4,7]
输出: 3
解释:
长度最长的公共子数组是 [3, 2, 1]。
"""
class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        if not nums1 or not nums2:
            return 0
        
        l1 = len(nums1)
        l2 = len(nums2)

        # 初始化dp数组， dp[A用了几个字符][B用了几个字符]
        dp = [[0] * (l2 + 1) for i in range(l1 + 1)]
        res = 0

        # 我们不用定义初始状态，因为dp[0][0]两个空字符串没有公共数组

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                # 当且仅当两个字符相等，我们才能在原有基础上继续更新
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

                # 因为我们要求连续，所以不能像1143(LCS)一样，可以把最近的状态的最值保留住
                # 不断更新最大结果
                if dp[i][j] > res:
                    res = dp[i][j]
        return res

"""
https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/solution/dong-tai-gui-hua-by-hai-gen/
"""