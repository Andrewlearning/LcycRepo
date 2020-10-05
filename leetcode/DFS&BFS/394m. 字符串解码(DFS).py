"""
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

**这个规则很重要：
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

 

示例 1：

输入：s = "3[a]2[bc]"
输出："aaabcbc"

"""
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.helper(s, 0)[1]

    def helper(self, s, p):
        res = ""
        multi = 0

        while p < len(s):
            if s[p] == "[":
                # 我们得到]的下标，直接可以跳过去
                # 并且得到括号里的值
                p, temp = self.helper(s, p + 1)
                # 乘上括号里的值
                res += multi * temp
                # 更新乘数
                multi = 0

            # 假如s[p] = ], 说明p已经到]位上了，而且res已经记录了[。。]里的所有字母了，可以返回了
            elif s[p] == "]":
                return p, res

            # 假如说碰到数字，那就更新到multi里去
            elif s[p].isdigit():
                multi = multi * 10 + int(s[p])
            # 假如说碰到字母，那就老老实实加到res里去
            elif s[p].isalpha():
                res += s[p]
            p += 1

        return p, res

# 链接：https://leetcode-cn.com/problems/decode-string/solution/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/
