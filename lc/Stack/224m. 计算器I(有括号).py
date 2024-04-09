class Solution:
    def helper(self):
        # self.nums = [..,x,y]
        y = self.nums.pop(-1)
        x = self.nums.pop(-1)
        sign = self.ops.pop(-1)

        # 把局部计算结果加回到self.num里
        if sign == "+":
            self.nums.append(x + y)
        elif sign == "-":
            self.nums.append(x - y)

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.p = {'(': 0, ')': 0, '+': 1, '-': 1}
        self.ops = []
        self.nums = []
        
        # 清除掉字符串里所有的空格, 为后面判断是否是负数的时候提供作用
        r = ""
        for c in s:
            if c != " ":
                r += c
        s = r
        
        i = 0
        while i < len(s):
            char = s[i]
            """
            +-*\^: while 栈顶符号优先级 >= 当前符号的优先级
                    那说明要先算栈里面的
                运算至栈顶符号优先级 < 当前符号优先级，才把当前运算符压入栈中
            """
            if char in "+-*/":
                # case1: -1, i=0, 要往开头加0，变为0-1
                # case2: (-1, i=2, 要往-1前加0，变为(0-1
                if i == 0 or s[i - 1] in '(+-':
                    self.nums.append(0)
                while len(self.ops) > 0 and self.p[self.ops[-1]] >= self.p[char]:
                    # debug用
                    # (1+(4+5 + ['(', '+', '(', '+']
                    # (1+(4+5+2) - ['(', '+']
                    # print(s[:i], char, self.ops)

                    self.helper()
                self.ops.append(char)
            elif char == "(":
                self.ops.append(char)
            elif char == ")":
                # 假如栈顶不是(, 说明()里的数还没算完，需要算一遍
                # 算到直到只剩下 ( x，退出循环
                while len(self.ops) and self.ops[-1] != "(":
                    self.helper()

                # debug用 
                # print(char, s[:i+1], self.ops)

                # 然后把 "(" 给pop掉，那么一个括号里的数就全部算完了
                self.ops.pop(-1)
            elif char.isdigit():
                # 处理数字，把一个完整的数字(int[i:j])给丢到栈里去, 例如 +100, 要把100都处理进去
                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1
                self.nums.append(int(s[i:j]))
                i = j - 1


            i += 1

        while self.ops:
            # "(1+(4+5+2)-3)+(6+8)" -> 到这只剩下 [9,4] ['+'], 要最后再计算一次
            # debug 用
            # print(self.nums, self.ops)
            self.helper()

        return self.nums[-1]


# https://www.acwing.com/video/1596/
# 原来的讲解有点过时，没有考虑到负数的情况，例如 -1 + 2, 或 2 + (-1), 目前版本已完善可以处理
# 参考了这个答案 https://www.acwing.com/activity/content/code/content/7398809/