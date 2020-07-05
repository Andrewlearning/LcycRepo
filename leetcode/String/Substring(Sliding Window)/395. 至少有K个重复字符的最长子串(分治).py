"""
找出一个字符串T的最长连续子字符串，要求这个子字符串中每个字符出现的次数都最少为K，
求出这个子字符串的最长长度。

输入:
s = "ababbc", k = 2

输出:
5

最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
"""
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if s < k:
            return 0

        for char in set(s):
            # 如果当前字符串s，出现了小于k次的字符，那么我们就要把那个字符剔除
            # 然后看剔除那个字符以后，每一个分段
            # 哪一个分段，是满足要求且最长的
            if s.count(char) < k:
                return max([self.longestSubstring(part, k) for part in s.split(char)])

        # 假如说当前字符没有出现频率小于k的字符，那么说明当前串是满足要求的
        # 直接返回当前串的长度
        return len(s)

"""
这题用了分而治之的思想
https://blog.csdn.net/fuxuemingzhu/article/details/82889933
答案：
1.如果字符串s的长度少于k，那么一定不存在满足题意的子字符串，返回0；
2.如果一个字符在s中出现的次数少于k次，那么所有的包含这个字符的子字符串都不能满足题意。所以，应该去不包含这个字符的子字符串继续寻找。这就是分而治之的思路，返回不同子串的长度最大值。

3.如果s中的每个字符出现的次数都大于k次，那么s就是我们要求的字符串。
"""