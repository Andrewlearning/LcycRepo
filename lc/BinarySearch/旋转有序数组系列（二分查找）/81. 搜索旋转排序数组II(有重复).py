"""
(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search.
If found in the array return true,
otherwise return false.

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
这个是带重复数字的二分搜索
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return -1

        # 由于这题允许数字重复，所以nums的开头部分和结尾部分有可能相等
        # 这会使得二分的性质失效，所以我们把nums末尾与开头相同的数都pop掉
        # 其余部分和33题一样
        while len(nums) > 1 and nums[0] == nums[-1]:
            nums.pop()

        n = len(nums)
        l = 0
        r = n - 1

        # 找到上升区间和下降区间的分解点
        while l < r:
            mid = (l + r + 1) // 2
            # 我们要找到，满足这个条件的最右点，所以是找右边界
            if nums[mid] >= nums[0]:
                l = mid
            else:
                r = mid - 1

        # 当退出循环时，我们就已经找到一个上升区间的最后一个元素
        # 然后我们要判断target再哪个区间，再来决定在哪个区间进行二分

        # target在上升区间, l = 0, r = 上升区间最后一个元素
        if target >= nums[0]:
            l = 0
        # target在下降区间, l = 上升区间最后一个元素 + 1, r = n - 1
        else:
            l = r + 1
            r = n - 1


        # 这里只是单纯为了找到target, 用左区间模板和右区间模板都没啥所谓
        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1

        # 为什么这里用r, 因为在假如输入数组只有一个元素的l=r+1会导致越界
        # 所以这里用r
        if nums[r] == target:
            return True
        else:
            return False
"""
best O(logn) worstO(n)-当所有数都一样的时候 space:O(1)
https://www.acwing.com/video/1425/
"""