"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
在algocast里有用二分查找的做法（ONlogN）
这里在算法通关40讲里面介绍的是递归的做法
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        if nums is None or len(nums) == 0:return

        res = 1

        # 表示到当前位置上，最长且不连续的递增子串长度是多少
        dp = [1 for i in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i,-1,-1):
                # 假如说我们发现当前字母[i], 大于之前的某个字母[j]
                # 那么我们就要看是否能更新dp[i]的最大值
                if dp[j] < dp[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

            # 因为dp[-1]不代表拥有最长子串，所以我们要记录每一次的最大值
            res = max(res,dp[i])

        return res

"""
https://www.youtube.com/watch?v=bQ6Y4WQjZVY&list=PLyIjPezcZJNNcmV2N3ZSypT00t7o2oSS-&index=50
"""