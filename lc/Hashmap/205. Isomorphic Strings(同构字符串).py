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

            # 一个字典为什么不够，因为可以 "a" -> "a" and "b" -> "a", 不能反映一对一的关系
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

以 s = "ab", t = "aa" 为例：
使用两个哈希表：
遍历到 s[0] = 'a', t[0] = 'a'：
sToT['a'] = 'a'
tToS['a'] = 'a'

遍历到 s[1] = 'b', t[1] = 'a'：
检查 sToT['b'] 是否已经存在：不存在，记录 sToT['b'] = 'a'。
检查 tToS['a'] 是否已经存在：已经存在，且 tToS['a'] = 'a'，但当前 s[1] = 'b'，与之前的映射 'a' -> 'a' 冲突。
因此，返回 false。
"""













