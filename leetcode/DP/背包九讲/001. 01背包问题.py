"""
有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。

第 i 件物品的体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品数量和背包容积。

接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 件物品的体积和价值。
"""

# 思路来源
# 答案来源 https://www.acwing.com/solution/acwing/content/4129/

def bagO1():
    N, V = map(int, input().split())

    v = [0]
    w = [0]

    for i in range(N):
        comb = [int(i) for i in input().split()]
        v.append(comb[0])
        w.append(comb[1])


    # 初始化，先全部赋值为0，这样至少体积为0或者不选任何物品的时候是满足要求
    dp = [[0 for i in range(V + 1)] for j in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, V + 1):
            # 初始化第i个物品不选，因为有可能超容量
            dp[i][j] = dp[i - 1][j]

            # 判断背包容量是不是大于第i件物品的体积, 只有大于的情况下才能选择当前物品
            if j >= v[i]:
                # 在选和不选的情况中选出最大值
                dp[i][j] = max(dp[i-1][j], dp[i - 1][j - v[i]] + w[i])

    return dp[-1][-1]


"""
有 N件物品 和 一个最大重量为V的背包
第i件物品的重量为 v[i], 价值是w[i]
求解哪些物品装入背包可是价值总和最大
每种物品只能选一次


递推：
dp[i][j] 表示只考虑前i件物品，放入容量为j的背包可以获得的最大价值

dp[i][j] = max( dp[i-1][j], dp[i-1][j-v[i]] + w[i])

dp[i-1][j]表示不取第i件物品，前i-1个物品的价值是多少那价值就是多少
dp[i-1][j-v[i]] + w[i] 表示取第i件物品， 那么它的价值就为前i-1个物品的价值 + i的价值
                                                重量为前i-1个物品的重量 + i的重量

初始化：
初始化我们可以把所有东西都初始化为0


遍历方法：
    for i in range(1, n + 1):
        for j in range(1, v + 1):

这样的意思是，我们每次按顺序挑出一个物品， 依次测试看能不能放进 容量为j的背包（j递增）
由因为 是否放入当前物品的状态i， 都由是否放入上一个物品的状态i-1变来的
所以我们可以保证放入每个物品的数量都是1

为什么都要从1开始遍历呢？
http://www.seotest.cn/jishu/36062.html，参考这里的表格，我们可以发现
当不放入物品时，i = 0, dp[i][j++]永远为0
当背包体积为0时， j = 0, dp[i++][j]也永远为0
所以我们没必要去遍历

dp有状态转移，经常有 i = i-1 啥的，所以需要从1开始



所以公式就是:

    for i in range(1,N+1):
        for j in range(1,V+1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-v[i]] + w[i])
"""

def bagO1compress():
    N, V = map(int, input().split())

    v = [0]
    w = [0]

    for i in range(N):
        comb = [int(i) for i in input().split()]
        v.append(comb[0])
        w.append(comb[1])


    # 初始化，先全部赋值为0，这样至少体积为0或者不选任何物品的时候是满足要求
    dp = [0 for j in range(V + 1)]

    for i in range(1, N + 1):
        for j in range(V, -1, -1):
            # 初始化第i个物品不选，因为有可能超容量
            if j >= v[i]:
                # 在选和不选的情况中选出最大值
                dp[j] = max(dp[j], dp[j - v[i]] + w[i])

    return dp[-1]



"""
如何进行空间压缩
我们可以把 dp[i][j] 变为 dp[j] 表示放入容量为j的背包可以获得的最大价值

dp[j] = max(dp[j], dp[j - v[i]] + w[i]) 
dp[j]表示不取第i件物品，前i-1个物品的价值是多少那价值就是多少
dp[[j-v[i]] + w[i] 表示取第i件物品， 那么它的价值就为前i-1个物品的价值 + i的价值
                                    前j个物品的价值为 dp[j - v[i]]

为什么遍历j的时候要从后往前？
因为我们使用dp自身作为一种动态压缩
所以当 dp[j] = max(dp[j], dp[j - v[i]] + w[i])时， dp[j]是作为现在的状态，但是dp[j - v[i]] + w[i]是作为上一次的状态

假如j 从前往后遍历的话，那么dp[j] = dp[j - v[i]] + w[i]， dp[j]是作为上一次的状态，dp[j - v[i]] + w[i]是作为本轮的状态
无法完成

一个例子：
[0, 2, 2, 2, 2, 2]
[0, 2, 4, 6, 6, 6]
[0, 2, 4, 6, 6, 8]
[0, 2, 4, 6, 6, 8]
"""

