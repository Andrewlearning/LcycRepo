"""
https://www.acwing.com/video/332/

f[i][j] 表示前i个整数（1,2…,i）恰好拼成结果j的方案数

利用了完全背包的思想
f[i][j]   = f[i-1][j] + f[i-1][j-1] + f[i-1][j-i*2] + ... + f[i-1][j-i*s]
f[i][j-1] =             f[i-1][j-1] + f[i-1][j-i*2] + ... + f[i-1][j-i*s]

所以根据上两式可以推出：
f[i][j] = f[i-1][j] + f[i][j-1]
"""

if __name__ == "__main__":

    n = int(input())
    mod = int(1e9 + 7)
    # f[i][j] 表示前i个整数（1,2…,i）恰好拼成j的方案数
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # 假如一个数都不选的话，那么就是一种方案，这个作为dp的状态初始化
    for i in range(0, n + 1):
        dp[i][0] = 1

    # 从第一个物体开始找
    for i in range(1, n + 1):
        # 利用前i个数，可以拼成总和为j
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] % mod

            if j >= i:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - i]) % mod

    print(dp[n][n])

    # https://www.acwing.com/video/332/
    # code https://www.acwing.com/activity/content/code/content/320392/