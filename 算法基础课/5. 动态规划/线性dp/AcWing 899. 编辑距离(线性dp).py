"""
对于每次询问，请你求出给定的n个字符串中有多少个字符串可以在上限操作次数内经过操作变成询问给出的字符串。

每个对字符串进行的单个字符的插入、删除或替换算作一次操作。

输入格式
第一行包含两个整数n和m。

接下来n行，每行包含一个字符串，表示给定的字符串。

再接下来m行，每行包含一个字符串和一个整数，表示一次询问。

字符串中只包含小写字母，且长度均不超过10。

输入样例：
3 2
abc
acd
bcd
ab 1
acbd 2
输出样例：
1
3
"""

def minDistance(word1, word2):
    if not word1 and not word2: return 0

    m = len(word1)
    n = len(word2)

    # dp[i][j] i表示word1的1-i的片段，j表示word2的1-j的片段，合在一起的意思就是
    # word1的1-i的片段 和 word2的1-j的片段，把他们变成相同的字符串最少需要多少步操作
    dp = [[0] * (n + 1) for i in range(m + 1)]

    # 边界值，假如说 "" , "abcd" , 那么dp要进行初始化设定, 最极端情况下要更改多少次
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # 检测出"a",""这种情况，直接返回结果
    if n == 0 or m == 0:
        return dp[m][n]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1),
                           dp[i - 1][j] + 1,
                           dp[i][j - 1] + 1)
    return dp[m][n]


if __name__ == "__main__":
    n, m = map(int, input().split())

    words = []
    for _ in range(n):
        words.append(input())

    res = 0
    for _ in range(m):
        res = 0
        curWord, limit = input().split()
        limit = int(limit)

        for otherWord in words:
            if minDistance(curWord, otherWord) <= limit:
                res += 1

        print(res)

# https://www.acwing.com/video/331/


