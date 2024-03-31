"""
给定两个表示复数的字符串。

返回表示它们乘积的字符串。注意，根据定义 i2 = -1 。

示例 1:

输入: "1+1i", "1+1i"
输出: "0+2i"
解释: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。
"""

class Solution:
    def complexNumberMultiply(self, x, y):
        a, b = self.breaker(x)
        c, d = self.breaker(y)

        # (a+bi) * (c + di) = a*c + a*di + cbi + bdi**2
        return str(a * c - b * d) + "+" + str(a * d + b * c) + "i"

    def breaker(self, string):
        i = string.index("+")
        # "a+bi"
        a = int(string[:i])
        b = int(string[i + 1:-1])
        return a, b

# https://www.acwing.com/video/1995/