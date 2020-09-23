"""
给出一个按 非递减 顺序排列的数组 nums，和一个目标数值 target。(递增)
假如数组 nums 中绝大多数元素的数值都等于 target，则返回 True，否则请返回 False。
"""
class Solution(object):
    def isMajorityElement(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False

        # 找到target的对应的最左下标
        lindex = self.binarySearchForLeft(nums, target)

        # 把边界条件判断完以后再进行求解
        if lindex != -1 and lindex + len(nums) // 2 < len(nums) and nums[lindex + len(nums) // 2] == target:
            return True

        return False

    def binarySearchForLeft(self, nums, target):

        l = 0
        r = len(nums) - 1
        index = -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

            if nums[mid] == target:
                index = mid

        return index

"""
Time O(logn), Space O(1)
本解法为最优解
因为数组顺序为递增，所以我们可以想到使用二分查找
本题的解体思路是 先通过二分查找找到target在数组的左边界（34题）
然后再通过 nums[lindex + len(nums) // 2] == target 检查是否超过半数的元素是不是target


"""