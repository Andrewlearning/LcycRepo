"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs and len(strs) == 0:
            return ""

        length = len(strs)

        # 第一个单词
        first = strs[0]

        # 我们按照第一个单词的长度来进行遍历，依次比对每个单词的bit
        for i in range(len(first)):

            # 从第二个单词开始，依次和第一个单词进行比对
            for j in range(1, length):

                # 当第一个单词的长度长于后面的单词的时候， 我们应该返回 first[:i]
                # 又或者当两个单词在 第i个字符不相等的时候，我们应该返回first[:i]
                if i >= len(strs[j]) or first[i] != strs[j][i]:
                    return first[:i]

        # 假如说以上流程都没有提前结束，那么说明first就是strs里最短的前缀，返回
        return first


"""
Time: O(k*n), Space: O(1)
https://algocasts.io/episodes/D1mRAeWz
"""

