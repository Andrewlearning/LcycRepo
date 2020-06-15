"""
Given a string, determine if it is a palindrome,
considering only（只考虑，说明遇到符号那些可以跳过） alphanumeric（数字和字母）
characters and ignoring cases（忽略大小写）.
"""
class Solution(object):
    def is_alphanumeric(self, char):
        return ("a" <= char <= "z") or \
               ("A" <= char <= "Z") or \
               ("0" <= char <= "9")

    # 假如出现大小写的情况，我们把两个字母都转换成大写的形式，来统一进行比较
    def convertLowtoHigh(self, a, b):
        convert = ord("a") - ord("A")
        if "a" <= a <= "z":
            a = chr(ord(a) - convert)
        if "a" <= b <= "z":
            b = chr(ord(b) - convert)

        return a == b

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None and len(s) == 0:
            return True

        i = 0
        j = len(s) - 1
        while i < j:

            # 跳过不合法的字母
            while i < j and not self.is_alphanumeric(s[i]):
                i += 1
            while i < j and not self.is_alphanumeric(s[j]):
                j -= 1

            # 转换成统一格式来进行比较
            if i < j and not self.convertLowtoHigh(s[i], s[j]):
                return False
            i += 1
            j -= 1

        return True

"""
https://algocasts.io/episodes/4rpaqpZb
Time: O(n), Space: O(1)
答案：
1.is_alphanumeric用于检测char是否满足题目要求的alphanumeric
2.is_ignoring_case用于检验字母是否回文（自动转换为大写用于比较）
3.双指针，左右同时向中间检查，满足条件return
"""
