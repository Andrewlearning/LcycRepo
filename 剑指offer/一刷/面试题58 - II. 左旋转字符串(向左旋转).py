""""
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。
比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

示例 1：

输入: s = "abcdefg", k = 2
输出: "cdefgab"
示例 2：

输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"

"""


class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        s = list(s)
        length = len(s)
        n = n % length

        # 先把[0,n-1]翻转
        self.reverse(s, 0, n - 1)

        # 再把[n, length-1] 翻转
        self.reverse(s, n, length - 1)

        # 最后整体翻转
        self.reverse(s, 0, length - 1)

        return "".join(s)

    def reverse(self, s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

"""
本题可以和189对照观看

https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/solution/pythonti-jie-duo-chong-fang-shi-shi-xian-da-po-mia/
"""