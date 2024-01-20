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
        mm = {}

        for char in magazine:
            if char not in mm:
                mm[char] = 1
            else:
                mm[char] += 1

        for char in ransomNote:
            # 假如不存在，则说明无法构成
            if char not in mm:
                return False
            else:
                mm[char] -= 1
                # 假如构成magazine需要更多元素，则说明无法构成
                if mm[char] < 0:
                    return False

        return True

"""
https://leetcode.com/problems/ransom-note/discuss/85783/Java-O(n)-Solution-Easy-to-understand
Time:O(n) space:O(n)
答案：
操作和387题有点像，但是难度降低了很多
"""