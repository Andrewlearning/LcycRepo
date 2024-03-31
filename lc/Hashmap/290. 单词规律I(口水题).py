"""
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true

"""
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        hashmap = {}
        s = s.split()
        if len(pattern) != len(s):
            return Fase

        for i in range(len(pattern)):
            if pattern[i] not in hashmap:
                if s[i] not in hashmap.values():
                    hashmap[pattern[i]] = s[i]
                else:
                    return False
            else:
                if hashmap[pattern[i]] != s[i]:
                    return False

        return True
