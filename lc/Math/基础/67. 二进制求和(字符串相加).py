"""
给你两个二进制字符串，返回它们的和（用二进制表示）。
输入为 非空 字符串且只包含数字 1 和 0。

示例 1:
输入: a = "11", b = "1"
输出: "100"

"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        pa = len(a) - 1
        pb = len(b) - 1
        carry = 0
        res = ""

        while pa >= 0 or pb >= 0 or carry:
            cur_sum = carry
            carry = 0

            if pa >= 0:
                cur_sum += ord(a[pa]) - ord("0")
                pa -= 1
            if pb >= 0:
                cur_sum += ord(b[pb]) - ord("0")
                pb -= 1

            if cur_sum >= 2:
                cur_sum -= 2
                carry = 1

            res += str(cur_sum)

        return res[::-1]

# 做法沿用其他求和类的题目