"""
现在，假设你分别支配着 m 个0和 n 个1。另外，还有一个仅包含0和1字符串的数组。

你的任务是使用给定的 个和 n 个1，找到能拼出存在于数组中的字符串的最大数量。
每个至多被使用一次。

输入: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
输出: 4

解释: 总共 4 个字符串可以通过 5 个 0 和 3 个 1 拼出，即 "10","0001","1","0" 。
"""
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        if not strs:
            return 0
        # 这题，用多少个0，和1是背包的容量，能拼出多少个字符串是价值
        # dp[i][j][k] [0-i]的字符串里，用j个0， k个1，能拼出多少个
        dp = [[[0 for k in range(n + 1)] for j in range(m + 1)] for i in range(len(strs) + 1)]

        for i in range(1, len(strs) + 1):

            zeros, ones = self.countZero(strs[i - 1])

            for j in range(0, m + 1):
                for k in range(0, n + 1):
                    dp[i][j][k] = dp[i - 1][j][k]

                    if zeros <= j and ones <= k:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - zeros][k - ones] + 1)

        return dp[-1][-1][-1]

    def countZero(self, string):
        res = [0, 0]

        for char in string:
            res[ord(char) - ord("0")] += 1

        return res


"""
https://leetcode-cn.com/problems/ones-and-zeroes/solution/dong-tai-gui-hua-zhuan-huan-wei-0-1-bei-bao-wen-ti/

那么本题如何进行空间压缩呢？
"""


class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        if not strs:
            return 0

        # dp[j][k]用j个0， k个1，能放多少
        dp = [[0 for k in range(n + 1)] for j in range(m + 1)]

        for i in range(1, len(strs) + 1):

            zeros, ones = self.countZero(strs[i - 1])

            for j in range(m, -1, -1):
                for k in range(n, -1, -1):
                    # 默认当前字符串无法拼凑，因为有可能超0,1的数量，
                    # 因为这里不操作的话，就默认当前的状态等于上一个状态了

                    if zeros <= j and ones <= k:
                        # 如果能操作当前的状态，是由上一个状态转变过来的
                        dp[j][k] = max(dp[j][k], dp[j - zeros][k - ones] + 1)

        return dp[-1][-1]

    def countZero(self, string):
        res = [0, 0]

        for char in string:
            res[ord(char) - ord("0")] += 1

        return res