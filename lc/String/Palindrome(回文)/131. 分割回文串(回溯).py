"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []
        self.res = []
        self.dfs(s, [])
        return self.res

    # 这里的string仅表示还没经历过分层的string
    def dfs(self, string, temp):
        if not string:
            self.res.append(temp[:])
            return

        for i in range(1, len(string)+1):
            # i从1开始主要是这里的原因，因为我们要使用切片，[:i]，i最少为1，切一次
            if self.check(string[:i]):
                # 我们发现string[:i]是回文的，所以把它添加进temp里，同时，把i及以后的字符串放进dfs里继续切割
                self.dfs(string[i:], temp + [string[:i]])

    def check(self, string):
        return string == string[::-1]

"""
https://www.youtube.com/watch?v=UFdSC_ml4TQ
"""