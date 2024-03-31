"""
给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。

 

示例 1：

输入："ab-cd"
输出："dc-ba"
示例 2：

输入："a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"
"""


class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type S: str
        :rtype: str
        """
        res = []
        j = len(s) - 1
        # 用j从后往前遍历字符串，碰到字母就append进res,因为j是后面的字母，append后等于变前了
        for i in range(len(s)):
            if s[i].isalpha():
                while not s[j].isalpha():
                    j -= 1
                res.append(s[j])
                j -= 1
            # 碰到符号就直接加进去，不进行处理
            else:
                res.append(s[i])

        return "".join(res)