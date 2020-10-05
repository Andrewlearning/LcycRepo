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


    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.priority = {'(': 0, ')': 0, '+': 1, '-': 1}
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

# https://www.acwing.com/video/1596/