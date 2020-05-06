"""
有 N 种物品和一个容量是 V 的背包。

第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
输出最大价值。

等于是物品有限额的完全背包问题，总体思路沿用完全背包，只不过我们需要加点数量限制
"""

# 参考https://www.acwing.com/solution/acwing/content/4451/

def bagO3():
    N, V = map(int, input().split())

    v = [0]
    w = [0]
    s = [0]


    for i in range(N):
        comb = [int(i) for i in input().split()]
        v.append(comb[0])
        w.append(comb[1])
        s.append(comb[2])

    dp = [0 for j in range(V + 1)]

    for i in range(1, N + 1):
        for j in range(V, -1, -1):
            # 在这里等于是加了数量的限制
            k = 1
            while k <= s[i] and k*v[i] <= j:
                    dp[j]= max(dp[j], dp[j - k*v[i]] + k*w[i])
                    k += 1

    return dp[-1]

"""
输入
4 5
1 2 3
2 4 1
3 4 3
4 5 2

[0, 0, 0, 0, 0, 0]
[0, 2, 0, 0, 0, 0]
[0, 2, 4, 0, 0, 0]
[0, 2, 4, 6, 0, 0]
[0, 2, 4, 6, 8, 0]
[0, 2, 4, 6, 8, 10]
"""