"""
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
"""
class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 343
        if n <= 3:
            return n - 1

        # 根据数学规律， 把数字分成三等分是最容易出最大积
        # 其次是 分成两等分
        a = n // 3

        # 下面这种情况考虑的是，当不能完全三等分的情况, 所余出来的值
        b = n % 3

        # 说明刚好可以三等分 a*a*a
        if b == 0:
            return int(pow(3, a))
        # 说明还是可以三等分 (a-1) * (a-1) * (a-1) * 4
        if b == 1:
            return int(pow(3, a - 1) * 4)
        # a * a * a * 2
        if b == 2:
            return int(math.pow(3, a) * 2)

# https://leetcode-cn.com/problems/integer-break/solution/343-zheng-shu-chai-fen-tan-xin-by-jyd/