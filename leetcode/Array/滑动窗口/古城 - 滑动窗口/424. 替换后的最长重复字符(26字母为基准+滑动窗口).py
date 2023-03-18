"""
给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。

注意:
字符串长度 和 k 不会超过 104。

示例 1:

输入:
s = "ABAB", k = 2

输出:
4

解释:
用两个'A'替换为两个'B',反之亦然。
"""

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0

        res = 0
        # 生成26个大写字母
        chars = [chr(ord("A") + i) for i in range(26)]

        # 每次循环，我们以一个字母作为基准，遇到不同于char的字母，都要变成char
        for char in chars:
            l = 0
            # 当前滑动窗口内，当前char的数量
            curCount = 0
            for i in range(len(s)):
                # 假如说右边界元素=char,说明在窗口内当前字母的出现次数+1
                if s[i] == char:
                    curCount += 1

                # 窗口内的所有元素-当前元素的数量 = 我们需要变化的元素数量
                # 我们需要变化的元素数量 > k的话，说明我们要缩小滑动窗口
                while (i - l + 1 - curCount) > k:
                    if s[l] == char:
                        curCount -= 1
                    l += 1

                res = max(res, i - l + 1)

        return res

# https://www.acwing.com/video/1829/