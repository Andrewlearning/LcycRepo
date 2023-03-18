"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
n为括号数量，要求要形成有效括号才能返回结果
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n is None:
            return []
        self.res = []
        self.helper(0, 0, n, "")
        return self.res

    def helper(self, left, right, n, string):
        if left == n and right == n:
            self.res.append(string)
            return
        if left < n:
            # 把 string + "(" 里面，等于完成了一次一次状态取消
            # 在下面right 拿到的string, 是没有加左括号的
            """
            string += "("
            self.helper(left + 1, right, n, string)
            string = string[:-1]
            """
            self.helper(left + 1, right, n, string + "(")
        if right < n and right < left:
            self.helper(left, right + 1, n, string + ")")


"""
https://www.youtube.com/watch?v=xtDjDTFk-Cw&list=PLyIjPezcZJNNcmV2N3ZSypT00t7o2oSS-&index=31
时间复杂度：O(2^n)

"""
