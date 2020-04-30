#!usr/bin/python
# -*- coding: utf-8 -*-
"""
写一个支持加减乘除的计算器
使得给出一个字符串，它能计算出里面的数值

输入: "3+2*2"
输出: 7
"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0

        op = "+"
        num = 0
        stack = []

        for i in range(len(s)):
            if "0" <= s[i] <= "9":
                num = num * 10 + int(s[i])

            if s[i] in "+-*/" or i == len(s) - 1:
                if op == "+":
                    stack.append(num)
                if op == "-":
                    stack.append(-num)
                if op == "*":
                    stack.append(stack.pop() * num)
                if op == "/":
                    # 这里是因为python2的语言特性问题
                    if stack[-1] < 0:
                        stack.append((stack.pop() + num - 1) / num)
                    else:
                        stack.append(stack.pop() / num)

                op = s[i]
                num = 0
        return sum(stack)

s = Solution()
s.calculate("14-3/2")



"""
Time: O(n), Space: O(1)
https://algocasts.io/episodes/n5GqBVpA

这道题的思想是， 把一个式子给分成好几部分的和，然后再相加
例如： 1+3 + 2*6/3 -2, 我们把它看成 1 3  2*6/2 -2 这四个整体
然后把每个整体处理完后放进stack里面去
最后求和
"""