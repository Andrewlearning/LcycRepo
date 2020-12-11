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
        if not nums or len(nums) == 0:
            return False

        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if target == nums[mid]:
                return True

            # 与33唯一不同的点，消除重复项
            elif nums[l] == nums[mid]:
                l += 1
                continue

            # 说明mid在左边的递增区间
            elif nums[l] <= nums[mid]:
                # 假如说target在这个范围内,缩小的范围到[l,mid)
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                # 假如说target不在这个范围内,我们把范围定位到(mid,r]
                else:
                    l = mid + 1

            # 说明mid在右边的递增区间
            elif nums[l] > nums[mid]:
                # 假如说target在这个范围内,缩小的范围到(mid,r]
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                # 假如说target在不在这个范围内,缩小的范围到[l,mid)
                else:
                    r = mid - 1

        return False

"""
best O(logn) worstO(n) space:O(1)
https://www.youtube.com/watch?v=e-UALGfQpOk
答案：
https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/yi-wen-jie-jue-4-dao-sou-suo-xuan-zhuan-pai-xu-s-2/
"""