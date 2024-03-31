"""
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

输入:
"abccccdd"
输出:
7
解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        #统计每个字母出现的次数
        hm = {}
        for c in s:
            if c not in hm:
                hm[c] = 1
            else:
                hm[c] += 1

        # 收集s可用于构造回文字符串的字母有几个
        res = 0
        for c in hm.keys():
            # 先获取在s中，有多少个偶数的字母
            # 把每个字母出现的次数 // 2并向下取整，例如 2,3 -> 1, 然后再*2
            # 这是因为我们要构造回文，所以有三个相同字母我们也只能用2个
            res += hm[c] // 2 * 2

        # 在此之前构造的回文串没有考虑中心点可以为奇数的情况
        # 假如发现s中不是所有字母都用上了，那么我们则可以在构造的回文串中心加一个单独的字母
        if res < len(s):
            return res + 1
        return res


"""
时间复杂度：O(N)，其中 N 为字符串 s 的长度。我们需要遍历每个字符一次。
空间复杂度：O(S)，其中 S 为字符集大小。

https://www.acwing.com/activity/content/problem/content/2807/1/Python3/
往简单里说，就是我们要构造一个回文串
回文串最长是 1个奇数+偶数， 例如 abcba

所以我们把能每个字母最多能取几个偶数给弄出来，全加进去
假如发现s中不是所有字母都用上了，那么我们则可以在构造的回文串中心加一个单独的字母
"""

