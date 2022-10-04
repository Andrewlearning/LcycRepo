"""
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.


Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.
"""
class Solution(object):
    def findMaxForm(self, strs, lz, lo):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        if not strs:
            return 0

        # dp[i][j] 表示在当前遍历到的strs元素范围内，在用i个0, j个1的前提下，最多能使用多少个子字符串
        dp = [[0] * (lo + 1) for _ in range(lz + 1)]

        # 枚举每个物品
        for s in strs:
            zeros, ones = self.countZero(s)

            # 从大到小枚举体积, 枚举范围[zeros, lz]个0, [ones, lo]个1
            for i in range(lz, zeros - 1, -1):
                for j in range(lo, ones - 1, -1):

                    # 假如我们不使用s, 那么dp[i][j] = dp[i][j], 所以我们可以省略
                    # 假如我们使用s, 那么dp[i][j] = dp[i - zeros][j - ones]
                    # max() 是表明我们从上面两种选法中取其中的最优解来记录
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        return dp[-1][-1]

    def countZero(self, string):
        res = [0, 0]
        for char in string:
            res[ord(char) - ord("0")] += 1

        return res

"""
这个答案是已经被压缩过纬度的
https://www.acwing.com/video/1882/
"""