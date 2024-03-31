"""
给定两个数组，编写一个函数来计算它们的交集。
返回的确实也是个交集

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [9,4]

"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return set(nums1) & set(nums2)

"""
时间复杂度：O(m+n)，其中 n 和 m 是数组的长度。
O(n) 的时间用于转换 nums1 在集合中，O(m) 的时间用于转换 nums2 到集合中
并且平均情况下，集合的操作为 O(1)。
空间复杂度：O(m+n)，最坏的情况是数组中的所有元素都不同。

链接：https://leetcode-cn.com/problems/intersection-of-two-arrays/solution/liang-ge-shu-zu-de-jiao-ji-by-leetcode/
处。
"""