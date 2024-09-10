"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.res = ""
        n = len(s)

        def expend(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                if j - i + 1 > len(self.res):
                    self.res = s[i:j + 1]
                i -= 1
                j += 1

        for i in range(n):
            expend(i, i)
            if i > 0:
                expend(i - 1, i)

        return self.res


"""
该算法的时间复杂度为 O(n²)，其中 n 是字符串 s 的长度。
分析：
    外层 for 循环遍历字符串中的每一个字符，总共执行 n 次。
    对于每个字符，调用两次 expend 函数（分别检查奇数长度和偶数长度的回文子串）。
    expend 函数中的 while 循环，最坏情况下在每次调用时会进行 O(n) 次字符比较。
    因此，外层循环执行 n 次，expend 函数的最坏时间复杂度是 O(n)，总体的时间复杂度为 O(n²)。

空间复杂度：
该算法的空间复杂度为 O(1)，因为除了存储结果的 self.res 字符串和一些辅助变量外，没有使用额外的空间。
"""
