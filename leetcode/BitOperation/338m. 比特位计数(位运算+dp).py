"""
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i 
计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]
示例 2:

输入: 5
等于是从0-5，每个数字的比特位有多少个1
输出: [0,1,1,2,1,2]
"""

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0] * (num + 1)

        for i in range(1, num + 1):
            # 例如要看 1101
            # 我们只用看 110有多少个1 + 1101上的个位是不是1
            dp[i] = dp[i >> 1] + (i & 1)

        return dp