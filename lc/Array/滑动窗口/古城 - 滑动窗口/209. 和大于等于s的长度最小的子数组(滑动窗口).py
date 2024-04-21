"""
Given an array of n positive integers and a positive integer s,
find the minimal length of a contiguous subarray(连续的子array) of which the sum ≥ s.
If there isn't one, return 0 instead.

Example:
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
"""
import sys
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        if not nums and len(nums) == 0:
            return 0

        # 我们采用的是利用[l, i]来表示滑动窗口
        l = 0
        res = float('inf')

        # 滑动窗口内的值
        # 得用一个值来记录滑动窗口内值的和
        # 利用sum()的话在一些特别大的case会超时
        wSum = 0

        for i in range(len(nums)):
            # 每次循环都往滑动窗口里添加元素
            wSum += nums[i]

            # 假如滑动窗口内的和 >= s了，说明我们可以缩小窗口了
            # 用while的原因是，有可能这个窗口可以缩小不止一次
            # 例如 [0,0,3,4] s = 7, 那么这个窗口就可以缩小两次
            while wSum >= s:
                res = min(res, i - l + 1)
                wSum -= nums[l]
                l += 1

        # 假如res没有更新，说明没有满足 >= s的子数组，返回0
        return 0 if res == float('inf') else res

"""
Time O(n) , space O(1)
我们可以对比一下209和325
209是一道典型的滑动窗口，因为它要求的值是大于等于某个值，所以我们可以利用while不断调整窗口
325是一道典型的前缀和问题，它要求的值是刚好等于某个值，假如说我们利用滑动窗口while调整窗口的做法
那么很容易一不满足while的条件，就退出循环，这样会错过大量的可能性，导致答案不精准
"""