"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
"""
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.remove(s, result, 0, 0, ('(', ')'))
        return result


    def remove(self, s, result, last_i, last_j, par):
        count = 0
        for i in range(last_i, len(s)):

            # s[i] == "("
            if s[i] == par[0]:
                count += 1

            # s[i] == ")"
            if s[i] == par[1]:
                count -= 1

            # 说明左括号比右括号多，说明还有戏，因为后续还有可能会有右括号进来
            if count >= 0:
                continue

            # 当count< 0, 右括号比左括号多，出错，进行删除
            # 从上一次被删除的元素后一位(last_j)出发，到当前位置i
            # 我们可以理解为，从[0 ~ last_j), 都是ok的，但是从[last_j, i],就有出错的现象
            for j in range(last_j, i + 1):

                # 当s[j]为右括号
                # 且，last_j就是 ） ， 那么肯定是错的 -> () )
                # 或， ) 前面一个字符不是 ), 那就意味着前一个字符可能是 ( 或者 a, 为什么？？？？？
                if s[j] == par[1] and (j == last_j or s[j - 1] != par[1]):
                    self.remove(s[:j] + s[j + 1:], result, i, j, par)
            return

        # 正向删除之后，有可能是左括号数量多于右括号，所以我们需要反转一遍，再检查
        # 一次
        reversed_s = s[::-1]
        if par[0] == '(':
            self.remove(reversed_s, result, 0, 0, (')', '('))
        else:
            result.append(reversed_s)

"""
思路来源：https://www.youtube.com/watch?v=llYfOsGSvdc
"""