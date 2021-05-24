
if __name__ == "__main__":
    n, m = map(int, input().split())
    text1 = input()
    text2 = input()

    # 初始化dp数组， dp[text1用了几个字符][text2用了几个字符]时最长公共子序列是多少
    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

    # 我们不用定义初始状态，因为dp[0][0]两个空字符串没有公共序列

    # 从两个字符串的第一个字符开始遍历
    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):

            # 假如两个字符相等
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            # 假如两个字符不相等，因为不要求连续
            # 我们只要把距离当前状态最近的两个状态的最值，转移到当前状态就好
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    print(dp[-1][-1])

# lc1143