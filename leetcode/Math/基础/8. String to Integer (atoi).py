"""
这个题目说的是，给你一个字符串，你要把它转成一个 int 类型的数字。这个字符串里可能会包含空格，字母或是其它字符。

一个可以有效地转成数字的字符串包含以下特点：
1. 可以有前导空格或前导 0，但不能有其它前导字符
2. 可能会有一个加号或减号表示正负，也可能没有，连续的多个加号或减号则视为不合法
3. 紧接着是一段连续的数字，如果没有数字则示为不合法
4. 数字后的其它字符都可以忽略
5. 如果数字大于 int 的最大值或小于 int 的最小值，返回相应的极值即可
6. 字符串如果不能合法地转为整数，则返回 0
"""
class Solution(object):
    def myAtoi(self, s):
        # strip的作用是去除字符串的前后空格
        s = s.strip()
        # 假如说str除空格后空了，说明这个str全是空格组成的，返回0
        if len(s) == 0:
            return 0

        # 判断s的符号
        sign = 1
        if s[0] in "-":
            sign = -1
        # 去除str的符号
        if s[0] in "+-":
            s = s[1:]

        res = 0
        for c in s:
            # 111&666，中途出现奇怪符号的，直接break
            if not c.isdigit():
                break
            # 我们用(ord(char) - ord("0"))来直接获取到 char当前位置的int
            res = res * 10 + (ord(c) - ord("0"))

        # 返回答案范围在[-2**31, 2*31-1], 假如超出这个范围，则返回超出的边界值
        return max(-2**31,min(2**31 - 1, sign*res))

"""
https://leetcode.com/problems/string-to-integer-atoi/discuss/203523/Python-solution-beats-93
"""