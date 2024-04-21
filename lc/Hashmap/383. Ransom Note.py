"""
Note:
You may assume that both strings contain only lowercase letters.
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
假如说前面的字符串能由后面的字符串构成（不需要连续），则放回True
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import defaultdict

        r = ransomNote
        m = magazine
        mm = defaultdict(int)
        rm = defaultdict(int)

        for c in r:
            rm[c] += 1
        for c in m:
            mm[c] += 1

        for k in rm:
            # 需要magazine不单包含ransomNote里的所有元素，且出现次数也要 >= ransomNote
            if k not in mm or rm[k] > mm[k]:
                return False
        return True

"""
https://leetcode.com/problems/ransom-note/discuss/85783/Java-O(n)-Solution-Easy-to-understand
Time:O(n) space:O(n)
答案：
操作和387题有点像，但是难度降低了很多
"""