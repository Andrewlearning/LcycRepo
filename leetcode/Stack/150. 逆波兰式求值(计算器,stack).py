class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                # 除数
                do = stack.pop(-1)

                # 被除数
                be_do = stack.pop(-1)

                if token == "+":
                    stack.append(do + be_do)
                elif token == "-":
                    stack.append(be_do - do)
                elif token == "*":
                    stack.append(be_do * do)
                # 整数除法只保留整数部分
                elif token == "/":
                    stack.append(int(float(be_do) / do))

        return stack.pop()


"""
注意，在python里面 遇到 -1/22 这种情况，还是会= -0.004xxxx
    但是这里要求的是 -1/22 = 0, 所以我们用 int(float(be_do) / do 来使-0.0004x变成0
"""