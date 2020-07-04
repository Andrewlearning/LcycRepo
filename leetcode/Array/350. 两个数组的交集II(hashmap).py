"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1:
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
与第一题的差别就是，这里是真的返回相同部分，而不是光返回一个set()

示例 2:
输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]

"""
import collections
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        n1, n2 = collections.Counter(nums1), collections.Counter(nums2)
        res = []

        for i in n1:

            # 本题关键点, 这里的设计害挺巧妙
            tmp = min(n1[i], n2[i])

            while tmp > 0:
                res.append(i)
                tmp -= 1

        return res

"""
本做法可以和1002放在一起看

时间复杂度：O(n+m)。其中n，m 分别代表了数组的大小。
空间复杂度：O(min(n,m))，我们对较小的数组进行哈希映射使用的空间
https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/solution/liang-ge-shu-zu-de-jiao-ji-ii-by-leetcode/


算法：
1. 把两个列表里的词频给统计出来
2. 然后挑一个来遍历
3. tmp: 1.假如说两个里面都有元素，那么挑词频小的那个出来
        2.假如只有其中一个里面有元素，同样挑小的出来，tmp = 0，无法进入while

4. 然后把少的那个数量，一个个得加进res里面去
"""

# 这题假如说给的两个数组是排序过的，那要怎么做？ 利用双指针
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        result = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):

            # 前两个都是为了 找到 nums[i] == nums[j]
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1

            # 当两个元素相等时
            else:
                result.append(nums1[i])
                i += 1
                j += 1

        return result

"""
时间复杂度：O(n+m)。其中 n，m 分别代表了数组的大小。
空间复杂度：O(min(n,m))，我们对较小的数组进行哈希映射使用的空间。


https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/solution/leetcode350-liang-ge-shu-zu-de-jiao-ji-ii-by-lsg-2/
"""
