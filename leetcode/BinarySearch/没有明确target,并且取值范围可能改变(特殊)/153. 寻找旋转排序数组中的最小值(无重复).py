"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

示例 1:

输入: [3,4,5,1,2]
输出: 1
"""
class Solution(object):
    def findMin(self, nums):

        if not nums or len(nums) == 0:
            return -1

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            # 说明小区间在mid的右边， 我们要[mid+1,r]
            if nums[mid] > nums[r]:
                l = mid + 1
            # 说明小区间在mid,或是mid左边，我们要[l,mid]
            elif nums[mid] < nums[r]:
                r = mid

        # l,r都可以
        return nums[r]


"""
看剑值offer6的解析
"""