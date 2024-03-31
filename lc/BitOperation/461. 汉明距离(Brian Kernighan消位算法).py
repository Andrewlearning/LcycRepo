"""
两个二进制数，每个位置上不同数 的数量的和
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
"""


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        # 相同位位0，不相同位为1
        new = x ^ y
        while new:
            # 统计有多少个不相同位，1 & 1 = 1，不相同位得到1
            count += new & 1
            new >>= 1
        return count


"""
time:O(n) space:O(1)
"""
