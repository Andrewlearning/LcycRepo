"""
"()(())"
output: 6

Input: ")()())"
Output: 4
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        res = 0


        for i in range(len(s)):
            # 当遇到左括号时，入栈
            if s[i] == "(":
                stack.append(i)

            # 当遇到")" 时， 我们把"(" 出栈
            # 但要是单纯 这样用这两者的下标相减，那么 遇到 ()()这种情况将无法处理
            # 所以我们需要保留 x ()(), X的信息，然后用最右边的的下标 - x的下标，得到答案
            else:
                stack.pop(-1)
                # 当栈为空且 s[i] = ")"时，它的作用是保留长度信息
                if len(stack) == 0:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])

        return res

"""
// Time: O(n), Space: O(n)
https://algocasts.io/episodes/n5GqbVpA
答案：
1.algocasts 里的p,代表的就是stack peek元素
2.
"""