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
        # 记录当前字符串每个字符所对应另一个字符串的字符
        sm = {} # key=schar, value=tchar
        tm = {} # key=tchar, value=schar
        n = len(s)

        for i in range(n):
            schar = s[i]
            tchar = t[i]

            if schar in sm:
                pre = sm[schar]
                if pre != tchar:
                    return False
            else:
                sm[schar] = tchar

            if tchar in tm:
                pre = tm[tchar]
                if pre != schar:
                    return False
            else:
                tm[tchar] = schar

        return True

"""
Time O(n) space O(0)
https://www.acwing.com/solution/content/315/
"""













