class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 我们让每个下标对应它应该要对应的数字 所以这个数组就有n+1
        # 然后k能取到左右极限，既是[1,n], 但是下面有用到k+1，所以要多加一位，长度为n+2
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        # 我们的最小子问题得是从2开始，因为从猜数范围从1开始的话，那就不用猜了
        # 就必然是那个数。
        # 到猜数范围为n+1结束
        for midRange in range(2, n + 1):
            # i是这个区间的左边界，从1开始
            i = 1
            while i + midRange - 1 < n + 1:
                # j是这个区间的右边界，最远到达n
                j = i + midRange - 1

                # 因为我们要取最小值，每个区间上的结果都定为正无穷
                dp[i][j] = float("inf")

                # 这里对k的边界限制有点模糊，因为我们的最小区间是2
                # 所以k既可以等于i, 也可以等于j
                for k in range(i, j + 1):
                    dp[i][j] = min(dp[i][j], max(dp[i][k - 1], dp[k + 1][j]) + k)

                i += 1

        return dp[1][n]

# https://www.acwing.com/video/1758/