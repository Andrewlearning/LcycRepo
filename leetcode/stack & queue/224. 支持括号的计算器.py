class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s and len(s) == 0:
            return 0

        # 代表一串数， 例如括号外的所有数字，或者括号内的所有数字
        res = 0

        # 初始化为正数
        sign = 1

        # 代表单个数
        num = 0
        stack = []

        for char in s:
            # num用于记录读取到的数字
            if char.isdigit():
                num = num * 10 + int(char)

            # 同样的，我们是先获得符号再获得数字 例如 3 + 4, 那么读取过程为 +3， +4
            elif char in ["-", "+"]:
                # 所以这里sign是上一个符号， num是当前读取到的数字
                res += sign * num

                # 用完sign和num后，我们可以重新赋值了
                sign = [-1, 1][char == "+"]
                num = 0


            elif char == "(":
                # 假如说是 4 + (5-5)
                # 首先我们先把res = 4加进stack
                stack.append(res)
                # 然后再把 “+” 加进stack
                stack.append(sign)

                # 然后初始化sign,和res,因为我们开始计算括号内的数了
                sign = 1
                res = 0

            elif char == ")":
                # 这里是把括号内的结果都计算进了res里面
                res += sign * num

                # 把括号内的处理完了，然后我们把括号外的再计算进去
                # 首先这里pop出来的是符号 -(4)
                res *= stack.pop()

                # 然后才pop出括号外的数字 3 -(4)
                res += stack.pop()

                # 最后把num清0
                num = 0

        # 例如 4 + 4, 因为最后一个4后面并没有符号了，所以没办法再把最后一个4给加进去了
        # 于是我们要在最后再加一次，这里的sign num,代表的是最后一次出现的符号和数字
        return res + sign * num

"""
https://leetcode.com/problems/basic-calculator/discuss/62424/Python-concise-solution-with-stack.
"""