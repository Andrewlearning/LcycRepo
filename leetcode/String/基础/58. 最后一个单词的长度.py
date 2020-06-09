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
        if not s and len(s) == 0:
            return 0

        end = len(s) - 1

        # 把字符串后面的空格给去掉
        while end >= 0 and s[end] == " ":
            end -= 1

        # "  "遇上这种情况
        if end < 0:
            return 0

        # 此时end停留在字符串最后一个单词的最后一个字母上
        start = end
        while start >= 0 and s[start] != " ":
            start -= 1

        # 此时start停留在最后一个单词的前一个空格上， " star" start = 0, end=4
        # 所以 4-0= 4
        return end - start
"""
https://leetcode-cn.com/problems/length-of-last-word/solution/hua-jie-suan-fa-58-zui-hou-yi-ge-dan-ci-de-chang-d/
"""