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
        if len(nums) == 0:
            return -1

        n = len(nums)
        l = 0
        r = n - 1

        # 找到上升区间和下降区间的分解点
        while l < r:
            mid = (l + r + 1) // 2
            # 我们要找到上升区间的最右点，既是满足这个条件的最右点，所以是找右边界
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

        # 为什么这里用r, 因为在假如输入数组只有一个元素时，l=r+1, r=n-1, 这个时候l=1,r=0
        # 会导致上面那个循环无法进入，所以nums[l=1]导致越界
        # 改成 if l > r or nums[l] != target: 也可以，因为当l > r时，说明异常情况发生
        if nums[r] == target:
            return r
        else:
            return -1

"""
https://www.acwing.com/video/1356/
1. 通过二分找到上升区间最后一个节点
2. 判断target在哪个区间
3. 通过二分找target的下标
"""




