"""
在一个给定的数组nums中，总是存在一个最大元素 。
查找数组中的最大元素是否至少是数组中每个其他数字的两倍。
如果是，则返回最大元素的索引，否则返回-1。

示例 1:

输入: nums = [3, 6, 1, 0]
输出: 1
解释: 6是最大的整数, 对于数组中的其他整数,
6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.
"""

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[m]:
                m = i

        for num in nums:
            if num != nums[m] and num * 2 > nums[m]:
                return -1
        return m

"""
Time： O(n)
Space: O(1)
https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/solution/zhi-shao-shi-qi-ta-shu-zi-liang-bei-de-zui-da-sh-8/

扫描数组找到唯一的最大元素 m，并记录它的索引 maxIndex。
再次扫描数组，如果我们找到 x != m，m < 2*x，我们应该返回 -1。
否则返回 maxIndex


"""