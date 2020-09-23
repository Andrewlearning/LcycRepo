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

        num = 0
        # 为啥不是-1，+1，因为这里有四种运算符
        # op仅代表上一次的数字
        op = "+"

        # stack用来放各个 符号*数字
        stack = []

        for i in range(len(s)):
            # 当我们遇到数字时，我们先把这个数字记录下来
            # 先记录数字的原因是
            # 我们把数字拆解成这样的形势 (+)14 (-)2 (*)3 这样加进栈里面
            # 到最后把它们都加起来
            if "0" <= s[i] <= "9":
                num = num * 10 + int(s[i])

            # 这里是起添加值的作用
            # s[i] in "+-*/" 当读取到符号的时候，我们要把上一个符号 * 上一个值加进stack
            # i == len(s) - 1 当读取到最后一个数字的时候， 我们要把上一个符号 * 最后一个数字加进stack
            if s[i] in "+-*/" or i == len(s) - 1:
                if op == "+":
                    stack.append(num)
                if op == "-":
                    stack.append(-num)

                # 在这里，乘除法的优先级比较高，所以他们不能直接放进栈里，和别的元素相加
                # 而是要把他们的优先级降下来，降到与 +-一样，再加入栈
                # 所以便有了以下的操作
                if op == "*":
                    stack.append(stack.pop() * num)
                if op == "/":
                    # 这里是因为python2的语言特性问题
                    # 例如 -3/2,我们想让它等于-1
                    # 但python算出来是等于-2的
                    if stack[-1] < 0:
                        stack.append((stack.pop() + num - 1) / num)
                    else:
                        stack.append(stack.pop() / num)

                # 上一次的op已经使用完了，把它更新成s[i],留给下一个num使用
                op = s[i]
                # 上一个num已经使用完了，把它变成0，用来给下一个num赋值
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