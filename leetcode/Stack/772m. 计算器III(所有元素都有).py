"""
实现一个基本的计算器来计算简单的表达式字符串。
表达式字符串只包含非负整数，+, -, *, /操作符，左括号 (，右括号 )和空格。整数除法需要向下截断。
你可以假定给定的字符串总是有效的。所有的中间结果的范围为 [-2147483648, 2147483647]。
示例 1：
输入：s = "2*(5+5*2)/3+(6/2+8)"
输出：21

"""
class Solution(object):
    def helper(self):
        # [x,y
        y = self.num.pop(-1)
        x = self.num.pop(-1)
        sign = self.op.pop(-1)
        if sign == "+":
            self.num.append(x + y)
        elif sign == "-":
            self.num.append(x - y)
        elif sign == "*":
            self.num.append(x * y)
        elif sign == "/":
            self.num.append(x / y)

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.priority = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2}
        self.op = []
        self.num = []
        i = 0
        while i < len(s):
            char = s[i]
            # 等于空格，跳过
            if char == " ":
                i += 1
                continue
            """
            +-*\^: while 栈顶优先级 >= 当前符号的优先级
                    那说明要先算栈里面的
                否则，或上面运算完后，把当前运算符压入栈中
            """
            if char in "+-*/":
                while len(self.op) > 0 and self.priority[self.op[-1]] >= self.priority[char]:
                    self.helper()
                self.op.append(char)
            elif char == "(":
                self.op.append(char)
            elif char == ")":
                # 假如栈顶不是(, 说明()里的数还没算完，需要算一遍
                while len(self.op) and self.op[-1] != "(":
                    self.helper()
                self.op.pop(-1)
            # char是数字，正常来说是碰到一个数字就算一次
            elif char.isdigit():
                # 处理数字，把一个完整的数字给丢到栈里去
                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1
                self.num.append(int(s[i:j]))
                i = j - 1

            i += 1

        while self.op:
            self.helper()

        return self.num[-1]

# 对应lintcode 849, 不过lintcode没有负数case，例如 -1 + (-2)
# https://leetcode-cn.com/problems/basic-calculator-iii/solution/shuang-zhan-fa-tong-yi-jie-jue-ji-ben-ji-suan-qi-s/