"""
只反转字符串里的元音字母"aeiou"（包括大写）
"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 0:
            return ""

        s = list(s)
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and s[right] not in vowels:
                right -= 1

            while left < right and s[left] not in vowels:
                left += 1

            s[left], s[right] = s[right], s[left]
            right -= 1
            left += 1

        return "".join(s)

"""
Time:O(n） SpaceO(n)
不知道有没有什么更好的做法

"""