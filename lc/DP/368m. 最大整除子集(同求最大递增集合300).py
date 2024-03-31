"""
给出一个由无重复的正整数组成的集合，找出其中最大的整除子集，子集中任意一对 (Si，Sj) 都要满足：Si % Sj = 0 或 Sj % Si = 0。

如果有多个目标子集，返回其中任何一个均可。

 

示例 1:

输入: [1,2,3]
输出: [1,2] (当然, [1,3] 也正确)
示例 2:

输入: [1,2,4,8]
输出: [1,2,4,8]
"""

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums and len(nums) == 0:
            return []

        nums.sort()
        # 我们假设每次都从当前数字开始，看看能形成的最长方案是多少
        dp = [1] * len(nums)

        # k记录着我们能形成的最大子集的下标在nums的哪里
        k = 0
        for i in range(len(nums)):
            for j in range(0, i):

                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                # 我们把能形成的最大子集下标更新到k
                if dp[i] > dp[k]:
                    k = i

        # 我们先把最大的那一位给加进答案
        res = [nums[k]]

        while dp[k] > 1:
            for i in range(k):
                # 我们要把刚刚的递推顺序从后往前找出来
                if nums[k] % nums[i] == 0 and dp[k] == dp[i] + 1:
                    # 然后把上一个怎么变过来的
                    # 加到res里去
                    res.append(nums[i])
                    k = i
                    break

        # res就是最长的递增子集方案了
        return res

# https://www.acwing.com/video/1754/