class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even = 0
        odd = len(nums) - 1

        while even < odd:
            while even < odd and nums[even] % 2 == 1:
                even += 1

            while even < odd and nums[odd] % 2 == 0:
                odd -= 1

            nums[odd], nums[even] = nums[even], nums[odd]

        return nums

"""
双指针，我们要把偶数向后面放，所以even要从左边开始，odd要从右边开始
"""



