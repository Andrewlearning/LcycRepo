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

        for i in range(1, len(nums)):
            # res[i-1]代表 nums[1~i-2]
            # res[i-1] * nums[i-1] 代表 nums[start ~ i-1]的乘积
            res[i] = res[i - 1] * nums[i - 1]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            # right 代表 nums[i+1 ~ end]的乘积
            res[i] *= right
            right *= nums[i]

        # 所以res[i] = res[i-1] * nums[i-1] * right
        # res[i] = nums[start ~ i-1] * nums[i+1 ~ end]
        return res

"""
https://algocasts.io/episodes/aVWyPJp2
// Time: O(n), Space: O(1)
"""