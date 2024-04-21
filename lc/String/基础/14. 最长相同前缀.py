"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串""。

示例1:

输入: ["flower","flow","flight"]
输出: "fl"
示例2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母a-z。
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 获取最短的单词的长度
        n = float('inf')
        for str in strs:
            n = min(n, len(str))

        # 假如最短长度=0，说明不可能有共同前缀
        if n == 0:
            return ""

        res = ""
        for i in range(n):
            cur = s[i]
            # 遍历每个单词，假如找到某一位不相等的话，那么就返回这一位前面的所有字母
            for s in strs:
                if s[i] != cur:
                    return res
            res += cur
        return res


"""
Time: O(k*n), Space: O(1)
"""

