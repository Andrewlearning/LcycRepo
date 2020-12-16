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

        # 左闭右闭区间
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid

        return l
"""
[1,3,5,6] target = 4
2.无target时，我们能返回非target的左界，[right]->3
3.无target时，我们能返回非target的右界，[left]->5

答案：
time: ologn
space: o1    
"""