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
        # 我们优先加左括号，这样才能保证能生成有效的括号
        if left < n:
            """
            string += "("
            self.helper(left + 1, right, n, string)
            string = string[:-1]
            """
            self.helper(left + 1, right, n, string + "(")
        # right < left 这个条件很重要，避免右括号生成在了左括号之前
        if right < n and right < left:
            self.helper(left, right + 1, n, string + ")")


"""
https://www.youtube.com/watch?v=xtDjDTFk-Cw&list=PLyIjPezcZJNNcmV2N3ZSypT00t7o2oSS-&index=31
时间复杂度：O(2^n)
"""

# 下面这种更常用的 append, pop写法，相对于上面的写法来说更复杂一点
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []

        def dfs(l, r, temp):
            if len(temp) > 2 * n:
                return
            if l == n and r == n:
                self.res.append("".join(temp[:]))

            if l < n:
                temp.append("(")
                l += 1
                dfs(l, r, temp)
                l -= 1
                temp.pop()
            if r < n and r < l:
                temp.append(")")
                r += 1
                dfs(l, r, temp)
                r -= 1
                temp.pop()

        dfs(0, 0, [])
        return self.res
