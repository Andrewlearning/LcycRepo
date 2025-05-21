"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums and len(nums) == 0:
            return 0

        n = len(nums)
        # 表示到当前位置上，最长且不连续的递增子串长度是多少
        dp = [1] * n
        res = 1

        for i in range(n):
            for j in range(i):
                # 假如说我们发现当前字母[i], 大于之前的某个字母[j]
                # 那么我们就要看是否能更新dp[i]的最大值
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

            # 更新最大值
            res = max(res, dp[i])

        return res

"""
dp做法时间复杂度 O(n^2)
文字可以看这个: https://leetcode.cn/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/
https://www.youtube.com/watch?v=bQ6Y4WQjZVY&list=PLyIjPezcZJNNcmV2N3ZSypT00t7o2oSS-&index=50
"""