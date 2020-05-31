"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321

"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign = 1 if x > 0 else -1
        x = abs(x)

        res = 0

        while x > 0:
            res = res * 10 + x % 10
            x //= 10

        if abs(res) > 2 ** 31:
            return 0

        return sign * res

"""
1.首先我们要返回一个数的相反数，我们得确定这个数是（正，负）-sign
2.之后我们让 x变为正数，为了不让其影响while循环的执行
3.while x != 0, 因为我们处理x的一位数，就要让它 x//=10,所以当x == 0时代表x已经被处理好了
4. res = x%10 + res*10, 把res放大，腾出个位给x%10
5. 处理异常情况， res的取值范围应该在 [−2^31,  2^31 − 1]之间
6. 返回res 时带上它应有的符号
"""