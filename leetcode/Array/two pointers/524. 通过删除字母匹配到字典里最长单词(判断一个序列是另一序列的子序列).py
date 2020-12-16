"""
给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。

示例 1:

输入:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

输出:
"apple"
示例 2:

输入:
s = "abpcplea", d = ["a","b","c"]

输出:
"a"
"""

class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        res = ""
        for string in d:
            # 是子序列
            if self.check(string, s):
                # 之前没答案
                # 当前比答案长
                # 长度相等但顺序比答案前
                # 更新
                if not res or len(string) > len(res) or (len(string) == len(res) and string < res):
                    res = string

        return res

    # 判断子序列
    def check(self, a, b):
        i = 0
        j = 0

        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                i += 1
            j += 1

        return i == len(a)