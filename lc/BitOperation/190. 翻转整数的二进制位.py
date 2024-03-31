class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if not n:
            return 0

        res = 0
        for _ in range(32):
            # 我们用n的最后一位和1去&
            # 假如n的最后一位是1，那么结果是1，附在res当前的位置上
            # 假如n的最后一位是0，那么结果是0，附在res当前的位置上
            res = (n & 1) | (res << 1)

            # 然后把n操作完的这一位给删掉，从左的补位是0
            n >>= 1

        return res

"""
// Time: O(1), Space: O(1)
https://www.youtube.com/watch?v=K0EHvvbUdEg
这个的原理和翻转整数是有点像的：
10进制
res = res*10 + n%10
n /= 10

二进制：
res = res*2 + n%2
n /= 2
其实上面这个操作和下面的是一样的
res = res<<1 | n&1
n >>= 1
"""