"""
给你一个仅包含小写字母的字符串，请你去除字符串中重复的字母
使得每个字母只出现一次。需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"
"""

import collections


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        res = []
        in_stack = collections.defaultdict(bool)
        last_index = collections.defaultdict(int)

        # 把每个char最后出现的index给记录下来
        for i in range(len(s)):
            last_index[s[i]] = i

        for i in range(len(s)):
            # 假如说s[i]已经在结果集里了
            # 说明到目前为止没问题,跳过
            if in_stack[s[i]]:
                continue

            # 例如 cac
            # 第一个c在结果集里，且c的字典序大于a, 且在a下标后面还有别的c，那么证明第一个c应该删掉
            # 我们按照上面操作，把a前面满足上面条件的元素全部去除
            while res and res[-1] > s[i] and last_index[res[-1]] > i:
                in_stack[res[-1]] = False
                res.pop(-1)

            res.append(s[i])
            in_stack[s[i]] = True

        return "".join(res)