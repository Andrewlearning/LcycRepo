"""
Suppose an array sorted in ascending order is rotated
at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return -1

        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if target == nums[mid]:
                return mid
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
        return -1


"""
https://algocasts.io/episodes/6emEOjpV
time O(logn) space O(1)
"""




