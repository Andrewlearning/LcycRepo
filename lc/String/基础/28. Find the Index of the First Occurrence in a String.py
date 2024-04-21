"""
Return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 两个字符串的长度
        lh = len(haystack)
        ln = len(needle)

        # 我们最多遍历前 [0 ~ lh - ln + 1],
        # +1是考虑到lh，ln 长度相等的情况，那么lh-ln=0，所以要+1来保证可以可以进行一轮遍历
        for i in range(lh - ln + 1):
            ph = i
            pn = 0

            while ph < lh and pn < ln and haystack[ph] == needle[pn]:
                ph += 1
                pn += 1

            if pn == ln:
                return i
        return -1

"""
Time:O(n * m) Space:O(1)
双指针的做法
"""


