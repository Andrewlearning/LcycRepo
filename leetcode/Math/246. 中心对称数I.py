"""
中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。

请写一个函数来判断该数字是否是中心对称数，其输入将会以一个字符串的形式来表达数字。

示例 1:

输入:  "69"
输出: true
"""

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        res = ""

        for char in num:
            if char in "23457":
                return False
            elif char == "6":
                res += "9"
            elif char == "9":
                res += "6"
            # 碰到0，1，8直接添加
            else:
                res += char

        # 最后反转看看想不想等
        return res == num[::-1]

"""
Time: O(n) Space: O(1)
这题没什么营养，属于口水题
"""