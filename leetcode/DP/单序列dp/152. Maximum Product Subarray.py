"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
连续子串相乘乘积为最大值
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxn = [0] * n
        minn = [0] * n
        maxn[0] = minn[0] = res = nums[0]

        for i in range(1, n):
            if nums[i] > 0:
                # 正 * nums[i](正) 容易得到最大值
                # 负 * nums[i](正) 那就使用nums[i]作为新的最大值
                maxn[i] = max(nums[i], nums[i] * maxn[i - 1])
                # 负 * nums[i](正) 容易得到最小值
                # 正 * nums[i](正) 那就使用nums[i]作为新的最小值
                minn[i] = min(nums[i], nums[i] * minn[i - 1])
            else:
                # 正 * nums[i](负) 那就使用nums[i]作为新的最大值
                # 负 * nums[i](负) 容易得到最大值
                maxn[i] = max(nums[i], nums[i] * minn[i - 1])
                # 正 * nums[i](负) 容易得到最小值
                # 负 * nums[i](负) 那就使用nums[i]作为新的最小值
                minn[i] = min(nums[i], nums[i] * maxn[i - 1])

            res = max(res, maxn[i])


"""
time O(n) space O(1)
答案：
我们始终维持祝一个maxi ,mini.两个变量。当一个数字加进来的时候，就看谁更大一点
"""
















