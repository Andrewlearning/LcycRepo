class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 0:
            return s

        #先去除多余的右括号
        s = self.helper(s, "(", ")")

        #再去除多余的做括号
        s = s[::-1]
        s = self.helper(s, ")", "(")

        #转回原来的位置返回
        return s[::-1]

    def helper(self, string, open, close):
        res = ""
        count = 0

        # 我们把多余的右括号先去除
        for char in string:
            if char == open:
                count += 1

            if char == close:
                if count <= 0:
                    continue
                count -= 1

            res += char

        return res

"""
https://leetcode-cn.com/problems/minimum-remove-to-make-valid-parentheses/solution/yi-chu-wu-xiao-gua-hao-by-leetcode/
时间复杂度：O(n)，其中 n 是输入字符串的长度。
空间复杂度：O(n)

这题可以看作是301的简化版，解题思想也是一样的
"""