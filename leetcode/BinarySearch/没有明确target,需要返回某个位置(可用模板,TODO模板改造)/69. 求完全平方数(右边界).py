"""
实现int sqrt(int x)函数。

计算并返回x的平方根，其中x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 本题的 目标是，找到一个最大的mid使得满足 mid**2 <= target, 这个mid就是答案
        # 所以等于是要找到一个符合范围的右边界
        l = 0
        r = x

        # 所以以下是求右边界的模板
        while l < r:
            mid = (l + r + 1) // 2

            if mid ** 2 <= x:
                l = mid
            else:
                r = mid - 1

        return l


"""
Time: O(log(n)), Space: O(1)
https://www.acwing.com/video/1407/
此题与leetcode367基本一样
"""
