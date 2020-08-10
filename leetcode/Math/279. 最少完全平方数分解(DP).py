class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        # dp数组初始化，初始化每个数只能由 1**2 组成
        dp = [i for i in range(n + 1)]

        for i in range(n + 1):
            # 我们先从1*1开始尝试，然后到2*2,3*3...
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        return dp[-1]


"""
https://algocasts.io/episodes/VXGOwEGQ
Time: O(n ^ 3/2), Space: O(n)
答案：
1. 已知任何数，都可以被完全平方数分解，因为任何数字，都可以由无数个1构成（1是完全平方数）
   所以初始化时，dp[i] = i,代表最差的可能性
   
2. dp[i] 是代表i这个数，最少能被多少个完全平方数分解
3. 例如 12 - 可被9,4,1
   dp[12] = dp[12 - 1] + 1 = dp[11] + 1,
          = dp[12 - 4] + 1 = dp[8] + 1
          = dp[12 - 9] + 1 = dp[3] + 1
   我们从上面可以看出dp[12]可以被怎样分解
   于是我们要得到dp[12] 的最少分解数，是不是就是说dp[12] = min(dp[11],dp[8],dp[3]) + 1
   
"""