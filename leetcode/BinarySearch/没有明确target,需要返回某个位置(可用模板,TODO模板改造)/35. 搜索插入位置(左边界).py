"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.(如果target不在，则返回它应该插入的地方)

You may assume no duplicates in the array.

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
[1,3,5,6] target = 4
我们要找4的插入位置，就是要找, >= target区间的左边界
所以就是按照findleft的写法去写

答案：
time: ologn
space: o1    
"""