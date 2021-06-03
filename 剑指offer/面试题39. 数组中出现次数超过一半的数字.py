import collections

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        count = 1
        res = nums[0]

        for i in range(1, len(nums)):
            if count == 0:
                res = nums[i]
                count = 1
                continue

            if res == nums[i]:
                count += 1
            else:
                count -= 1

        return res

"""
对应leetcode169

"""