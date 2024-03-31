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
        inStack = collections.defaultdict(bool)
        # 该元素在数组里的最后的下标
        lastIndex = collections.defaultdict(int)

        # 把每个char最后出现的index给记录下来
        for i in range(len(s)):
            lastIndex[s[i]] = i

        for i in range(len(s)):
            # 假如说s[i]已经在结果集里了，跳过，因为不能重复
            # 而且假如前面没被删掉，说明满足最小字典序
            if inStack[s[i]]:
                continue

            # 例如 cac
            # 第一个c在stack里，且c的字典序大于a, 且在a后面还有c(重要，因为我们只能删除重复项)
            # 那么证明第一个c应该删掉
            # 我们按照上面操作，把a前面满足上面条件的元素全部去除
            while stack and stack[-1] > s[i] and lastIndex[stack[-1]] > i:
                inStack[stack[-1]] = False
                stack.pop()

            stack.append(s[i])
            inStack[s[i]] = True

        return "".join(stack)

# 这个stack并不是完美的单调栈，但是思想是是与单调栈相同的
# 例如这个case: s="cbacdcbc" res="acdb", 可以看到"acdb"并不是单调的
# 此题可以和402一起看
# https://www.acwing.com/video/1705/