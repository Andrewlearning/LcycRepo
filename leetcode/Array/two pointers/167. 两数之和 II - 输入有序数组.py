class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(nums) - 1

        while i < j:
            # j 在这里只往后退
            while i < j and nums[i] + nums[j] > target:
                j -= 1
            if nums[i] + nums[j] == target:
                return [i + 1, j + 1]
            # i 在这里只往前走
            i += 1

        return []

"""
Time: O(n), Space: O(1)
https://www.acwing.com/video/1545/
答案：
因为是排序的，所以直接用双指针来做。时间空间效率最高
"""