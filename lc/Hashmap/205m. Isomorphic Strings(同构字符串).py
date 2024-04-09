"""
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        sm = {}
        tm = {}

        for i in range(len(s)):
            sv = s[i]
            tv = t[i]

            if sv in sm and sm[sv] != tv:
                return False
            if tv in tm and tm[tv] != sv:
                return False

            # 讲究一个匹配，因为我们要让两个字符串的字母，在每一个位置上，都是可以相互替换的，出现频率一样
            # 所以每次在结尾都做个匹配，下次假如匹配不到则说明不满足题目要求
            sm[sv] = tv
            tm[tv] = sv

        return True

"""
Time O(n) space O(0)
https://www.acwing.com/solution/content/315/
"""













