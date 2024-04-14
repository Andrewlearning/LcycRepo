"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.(如果target不在，则返回它应该插入的地方)

You may assume no duplicates in the array.
You must write an algorithm with O(log n) runtime complexity.

Input: nums = [1,3,5,6], target = 5
Output: 2
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums and len(nums) == 0:
            return 0

        l = 0
        r = len(nums)  # 因为可以插在len(nums)的那个位置上，所以这里要保留

        # 目的是, 从前往后找，第一个 >= target数的位置。所以使用左边界做法
        while l < r:
            mid = (l + r) // 2

            # [l,target,mid] [mid+1, r]
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1

        return l
"""
https://www.acwing.com/video/1358/
假如: [1,3,5,6] target = 5, 那么这个5插入在index=2的位置
假如: [1,3,5,6] target = 4, 那么这个4也是插入在Index=2的位置
所以这个题的目的是，从前往后找，第一个 >= target数的位置。所以使用左边界做法

答案：
time: ologn
space: o1    

对于左右边界查找不到的情况
[1,3,5,6] target = 4
左边界做法返回, 2
右边界做法返回, 1
所以可见 [1,3(右),5(左),6]

"""
