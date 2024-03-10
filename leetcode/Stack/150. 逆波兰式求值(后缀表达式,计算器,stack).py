"""
根据 逆波兰表示法，求表达式的值。
有效的运算符包括+,-,*,/。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

说明：
整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。


示例1：

输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: 该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
"""


class Solution(object):
    def helper(self, op):
        r = self.num.pop(-1)
        l = self.num.pop(-1)
        if op == "+":
            self.num.append(l + r)
        elif op == "-":
            self.num.append(l - r)
        elif op == "*":
            self.num.append(l * r)
        elif op == "/":
            self.num.append(int(float(l) / r))

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        self.num = []

        for char in tokens:
            if char in "+-*/":
                self.helper(char)
            else:
                self.num.append(int(char))

        return self.num[-1]



"""
https://www.acwing.com/video/1522/
这就是逆波兰表达式的做法
遇到一个数，把它加到栈顶
遇到一个符号，就把栈顶元素取出来处理一下


注意，在python里面 遇到 -1/22 这种情况，还是会= -0.004xxxx
    但是这里要求的是 -1/22 = 0, 所以我们用 int(float(be_do) / do 来使-0.0004x变成0
"""