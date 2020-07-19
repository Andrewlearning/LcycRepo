"""
给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及 * 。

示例 1:

输入: "2-1-1"
输出: [0, 2]
解释:
((2-1)-1) = 0
(2-(1-1)) = 2
"""
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        # 假如说切割到最后，input已经是只剩数字而没有符号了
        if input.isdigit():
            # 那么我们返回那个数字
            return [int(input)]

        res = []

        for i in range(len(input)):
            if input[i] in "+-*":
                # 当i为符号时，我们要以这个符号的左右来进行切割，最后直到left,right切割成只剩下数字
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])

                # 已知 left(数字) i（符号）right(数字)
                print(left, right)
                for x in left:
                    for y in right:
                        res.append(self.helper(int(x), int(y), input[i]))

        # 注意这里的res,并不是一个全局变量，所以当每个递归函数被调用的时候，他都会把当前的分组的值给返回到left,right
        return res

    def helper(self, x, y, sign):
        if sign == "+":
            return x + y
        elif sign == "-":
            return x - y
        elif sign == "*":
            return x * y
"""
https://www.youtube.com/watch?v=gxYV8eZY0eQ，看思路
https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/66419/Python-easy-to-understand-solution-(divide-and-conquer). 看解法
"""