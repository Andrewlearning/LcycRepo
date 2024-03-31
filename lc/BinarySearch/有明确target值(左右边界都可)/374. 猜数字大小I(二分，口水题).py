"""
就是一个最普通的二分查找
"""

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n

        while l < r:
            mid = (l + r) // 2

            # 相当于 mid >= target, 使用左边界的模板
            if guess(mid) in [-1, 0]:
                r = mid
            else:
                l = mid + 1
        return l
