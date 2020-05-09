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

        ans = 0

        #统计每个字母出现的次数
        count = collections.Counter(s)

        for v in count.values():
            #每个字母最多能取几个偶数给弄出来，全加进去
            ans += v // 2 * 2

            # 当我们的ans串是偶数的时候，且那个字母是有奇数个的时候，我们往答案里面加一个字母
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1

        return ans


"""
时间复杂度：O(N)，其中 N 为字符串 s 的长度。我们需要遍历每个字符一次。
空间复杂度：O(S)，其中 S 为字符集大小。

https://leetcode-cn.com/problems/longest-palindrome/solution/zui-chang-hui-wen-chuan-by-leetcode-solution/
往简单里说，就是我们要构造一个回文串
回文串最长是 1个奇数+偶数， 例如 abcba

所以我们把能每个字母最多能取几个偶数给弄出来，全加进去
然后当我们的ans串是偶数的时候，且那个字母是有奇数个的时候，我们往答案里面加一个字母
"""

