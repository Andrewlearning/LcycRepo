"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
"""


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""

        while n:
            n -= 1
            res += chr(n % 26 + ord("A"))
            n //= 26

        return res[::-1]

# https://algocasts.io/episodes/zbmKX5GZ
# 本题的难点是，假如说我们 %26， 那么出来的结果必然是在 [0,25]的
# 但是我们的要求是 [1,26]
# 例如28， 我们想要变成 AB
# 28 - 1 = 27, 27 % 26 = 1, 对应B
# 所以关键是这个n-1，但是构成数字母的