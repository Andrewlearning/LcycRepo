"""
Given a string, determine if it is a palindrome,
considering only（只考虑，说明遇到符号那些可以跳过） alphanumeric（数字和字母）
characters and ignoring cases（忽略大小写）.
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 统一大小写
        s = s.lower()
        l = 0
        r = len(s) - 1

        while l < r:
            # 跳过非字母数字
            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

"""
https://www.acwing.com/activity/content/code/content/659036/
Time: O(n), Space: O(1)
"""
