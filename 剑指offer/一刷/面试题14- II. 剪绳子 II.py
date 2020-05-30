class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n - 1

        # 根据数学规律， 把数字分成三等分是最容易出最大积
        # 其次是 分成两等分
        a = n // 3

        # 下面这种情况考虑的是，当不能完全三等分的情况, 所余出来的值
        b = n % 3

        # 本题特色，取模操作
        p = 1000000007

        # 说明刚好可以三等分 a*a*a
        if b == 0:
            return pow(3, a) % p
        # 说明还是可以三等分 (a-1) * (a-1) * (a-1) * 4
        if b == 1:
            return pow(3, a - 1) * 4 % p
        # a * a * a * 2
        if b == 2:
            return pow(3, a) * 2 % p

# https://leetcode-cn.com/problems/integer-break/solution/343-zheng-shu-chai-fen-tan-xin-by-jyd/