"""
给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。
示例 1:

输入: 5
输出: 2
解释: 5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2 。
示例 2:

输入: 1
输出: 0
解释: 1 的二进制表示为 1（没有前导零位），其补数为 0。所以你需要输出 0
"""

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num:
            return 0

        # 位数
        count = 0
        x = num
        while x:
            x >>= 1
            count += 1

        # 先对num取反
        # 然后根据有多少位，就与多少位1想与
        # 5 = 101  ~5 = 010
        # (1 << 3) - 1 = 111
        # 010 & 111 = 10
        return ~num & ((1 << count) - 1)

# https://www.acwing.com/video/1884/