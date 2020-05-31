"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

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
        # 本题的 目标是，找到一个mid使得 mid**2 == target
        l = 0
        r = x

        while l <= r:
            mid = (l + r) // 2

            if mid ** 2 == x:
                return mid

            # 说明要把mid变小
            elif mid ** 2 > x:
                r = mid - 1

            # 说明要把mid变大
            elif mid ** 2 < x:
                l = mid + 1

        # 这是二分搜索的特性，假如说因为指针交替而出循环，会形成 r [target] l这种局面
        return r



"""
Time: O(log(n)), Space: O(1)
https://algocasts.io/episodes/Z5mzEJWd
此题与leetcode367基本一样
"""