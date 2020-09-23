"""
给你一个仅包含小写字母的字符串，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

 

示例 1:

输入: "bcabc"
输出: "abc"
示例 2:

输入: "cbacdcbc"
输出: "acdb"
"""

import collections
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 结果集
        stack = []

        # 该元素是否在结果集里面
        in_stack = collections.defaultdict(bool)
        # 该元素在数组里的最后的下标
        last_index = collections.defaultdict(int)

        # 把每个char最后出现的index给记录下来
        for i in range(len(s)):
            last_index[s[i]] = i

        for i in range(len(s)):
            # 假如说s[i]已经在结果集里了，跳过，因为不能重复
            # 而且假如前面没被删掉，说明满足最小字典序
            if in_stack[s[i]]:
                continue

            # 例如 cac
            # 第一个c在结果集里，且c的字典序大于a, 且在a后面还有c，那么证明第一个c应该删掉
            # 我们按照上面操作，把a前面满足上面条件的元素全部去除
            while stack and stack[-1] > s[i] and last_index[stack[-1]] > i:
                in_stack[stack[-1]] = False
                stack.pop(-1)

            stack.append(s[i])
            in_stack[s[i]] = True

        return "".join(stack)

# https://www.acwing.com/video/1705/