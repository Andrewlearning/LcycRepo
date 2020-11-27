class Solution:
    def myPow(self, x, n):

        # 0^100 和 100^0 都是1
        if not x or not n:
            return 1

        # 负数的时候
        if n < 0:
            return 1/self.myPow(x,-n)

        # 次方数量为奇数的时候
        if n % 2 == 1:
            return x * self.myPow(x , n-1)

        # 次方数为偶数的时候
        if n % 2 == 0:
            return self.myPow(x*x , n//2)

"""
时间复杂度: O(logn)
空间复杂度：O(1)
"""

