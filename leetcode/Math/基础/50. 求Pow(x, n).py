"""
Implement pow(x, n),
which calculates x raised to the power n (xn).
计算 x**n
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        elif n < 0:
            return 1/self.myPow(x, -n)
        elif n % 2 == 1:
            return x * self.myPow(x, n-1)
        elif n % 2 == 0:
            return self.myPow(x*x, n//2)


"""
https://www.youtube.com/watch?v=UbUtaEUc9OY&list=PLyIjPezcZJNNcmV2N3ZSypT00t7o2oSS-&index=23
Time: O(log(n)), Space: O(1)
答案：
1.假如次方数n = 0，则返回1
2.假如说n <0,就意味着是倒数
3.n%2 == 1，说明是奇数次方，所以我们把一个n取出来，新递归为n-1
4.n>0 且 n为偶数，可以完成直接拆解

我们这样一次次拆一半来求(分而治之)，所以时间复杂度为O(logn),space O(1)
"""