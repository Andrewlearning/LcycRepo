"""
看leetcode69

给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

示例 1：

输入：16
输出：True
示例 2：

输入：14
输出：False
"""
class Solution(object):
    def isPerfectSquare(self, x):
        """
        :type num: int
        :rtype: bool
        """
        l = 0
        r = x

        # 如果找得到, 那么无论l,r的平方都是x
        # 如果找不到, 那么l ** 2 != x
        while l < r:
            mid = (l + r + 1) // 2

            if mid ** 2 <= x:
                l = mid
            else:
                r = mid - 1

        return l**2 == x

# 这题无论使用左模板还是右模板都可以成功，因为有一个明确的答案值