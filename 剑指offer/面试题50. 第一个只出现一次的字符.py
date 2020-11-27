"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:

s = "abaccdeff"
返回 "b"

s = ""
返回 " "
"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for c in s:
            # 假如字符第一次出现，那么 value = False
            # 假如字符不是第一次出现， 那么value = True
            dic[c] = not c in dic

        for c in s:
            # 找到第一个字符为True的返回就好了
            if dic[c] == True:
                return c

        return " "



"""
https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/solution/mian-shi-ti-50-di-yi-ge-zhi-chu-xian-yi-ci-de-zi-3/
"""