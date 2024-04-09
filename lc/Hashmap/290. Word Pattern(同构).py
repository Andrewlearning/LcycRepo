"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
从205题的同构字符串，变成290题的同构单词
"""


class Solution(object):
    def wordPattern(self, s, pattern):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = s.split(" ")

        hp = {}
        hs = {}

        if len(s) != len(pattern):
            return False

        n = len(s)
        for i in range(n):
            word = s[i]
            char = pattern[i]

            if char in hp and hp[char] != word:
                return False
            if word in hs and hs[word] != char:
                return False

            hp[char] = word
            hs[word] = char

        return True

"""
Time O(n) space O(n）
看205题就好了
"""