"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:
Input: "Hello World"
Output: 5
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        p = n - 1

        # 跳过末尾可能存在的空格 " hello world  "
        while p > -1 and s[p] == " ":
            p -= 1

        res = 0
        # 开始计算最后一个单词的长度
        while p > -1 and s[p] != " ":
            res += 1
            p -= 1

        return res