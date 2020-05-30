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

        class Solution(object):
            def isPerfectSquare(self, x):
                """
                :type num: int
                :rtype: bool
                """
                # 本题的 目标是，找到一个mid使得 mid**2 == target
                l = 0
                r = x

                while l <= r:
                    mid = (l + r) // 2

                    # 找得到return True
                    if mid ** 2 == x:
                        return True

                    # 说明要把mid变小
                    elif mid ** 2 > x:
                        r = mid - 1

                    # 说明要把mid变大
                    elif mid ** 2 < x:
                        l = mid + 1

                # 找不到，return False
                return False

"""
https://algocasts.io/episodes/Z5mzEJWd
"""