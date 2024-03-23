"""
Given a string s and a string t, check if s is subsequence of t.

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.
顺序得相同，但是不一定要是连续的，例如acd 是 abcd的subsequence
"""
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ps = pt = 0
        ns = len(s)
        nt = len(t)

        while ps < ns and pt < nt:
            if s[ps] != t[pt]:
                pt += 1
            else:
                ps += 1
                pt += 1

        if ps == ns:
            return True
        return False

"""
Time:O(n) space:O(1)
"""