"""
Given two strings s and t , write a function to determine
if t is an anagram（相同字母异序词） of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hs = {}

        # 构造可用的字母的map
        for c in s:
            if c not in hs:
                hs[c] = 1
            else:
                hs[c] += 1

        for c in t:
            if c in hs:
                hs[c] -= 1
                if hs[c] == 0:
                    # 假如这个可用的字母次数已经为0，那么直接删除掉
                    del hs[c]
            else:
                return False

        # 假如没有任何一个字母留下，刚好用完，则true
        return len(hs.keys()) == 0


"""

"""

