"""
问n是不是power of 3
"""
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 1是3的幂
        if n == 1:
            return True
        if n < 3:
            return False

        # 3 // 3 = 1，这个作为终止条件
        while n != 1:
            # 假如有数 %3 != 0说明不是3的幂
            if n % 3 != 0:
                return False
            n //= 3

        return n == 1
"""
与power of 2原理一样
"""
