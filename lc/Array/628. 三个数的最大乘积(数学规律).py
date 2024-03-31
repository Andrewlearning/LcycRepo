"""
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:

输入: [1,2,3]
输出: 6
示例 2:

输入: [1,2,3,4]
输出: 24
"""
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
        min1 = min2 = sys.maxsize
        max1 = max2 = max3 = -sys.maxsize
        for no in nums:
            if no < min1:
                min2 = min1
                min1 = no
            elif no >= min1 and no < min2:
                min2 = no
            if no > max3:
                max1 = max2
                max2 = max3
                max3 = no
            elif no <= max3 and no > max2:
                max1 = max2
                max2 = no
            elif no <= max2 and no > max1:
                max1 = no
                
        return max(max1*max2*max3, min1*min2*max3)

"""
# 链接：https://leetcode-cn.com/problems/maximum-product-of-three-numbers/solution/san-ge-shu-de-zui-da-cheng-ji-by-jie-fang-qu-de-ti/

"""
