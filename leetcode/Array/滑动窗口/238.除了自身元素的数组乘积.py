"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums and len(nums) == 0:
            return []

        res = [0] * len(nums)
        res[0] = 1

        # 构造res前缀乘积数组
        # res[i]代表 nums[0 ~ i-1] 的乘积
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        # right表示nums[i], 右侧所有数的乘积
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            # res[i] * right = nums[0 ~ i-1]的乘积 * nums[i+1 ~ -1]的乘积
            res[i] = res[i] * right
            right = right * nums[i]

        return res

"""
https://algocasts.io/episodes/aVWyPJp2
// Time: O(n), Space: O(1)
"""