"""
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。

示例:

输入: "Hello, my name is John"
输出: 5
解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。

"""


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s and len(s) == 0:
            return 0

        p = 0
        count = 0

        # 去掉前面空格，移动到第一个单词
        while p < len(s) and s[p] == " ":
            p += 1

        while p < len(s):
            count += 1
            # s[p]在单词里的话，则继续移动p
            while p < len(s) and s[p] != " ":
                p += 1

            # s[p]不在单词里，移动p
            while p < len(s) and s[p] == " ":
                p += 1

        return count