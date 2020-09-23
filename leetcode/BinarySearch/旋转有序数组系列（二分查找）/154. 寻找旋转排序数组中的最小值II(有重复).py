"""
Suppose an array sorted in ascending order(递增)is rotated at
some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
The array may contain duplicates.

Example:
Input: [2,2,2,0,1]
Output: 0

用153的代码会卡死在 [3,3,1,3] 上
Output: 3 | Expected:1
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0

        l = 0
        r = len(nums) - 1

        while l < r:

            mid = (l + r) // 2

            # mid 的右边一定又最小数字
            # 所以我们要 [mid+1, r]这个区间
            if nums[mid] > nums[r]:
                l = mid + 1

            # 说明 mid,right 在小区间，那么我们要慢慢缩小范围把范围变到[l,r-1]
            elif nums[mid] == nums[r]:
                r = r - 1

            # mid 的右边一定不是最小数字，mid 有可能是, mid的左边可能是，下一轮搜索区间是[left, mid]
            elif nums[mid] < nums[r]:
                r = mid

        # 这里放l,r都无所谓, 为什么
        return nums[l]

"""
https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solution/er-fen-jian-zhi-si-xiang-fen-zhi-si-xiang-by-liwei/
答案：
相比于153，只加一行代码
1.            if nums[mid] == nums[right]:
                right -= 1
原理和81一样，把分组的干扰项给去除掉再重新开始移动指针

注意，这种题去重的关键在于，第一个if 语句，是用哪两个指针进行判断的，如果那两个指针一开始出现
相同情况的话，就会出现分区错误，导致指针去错地方。81和154都一样
"""