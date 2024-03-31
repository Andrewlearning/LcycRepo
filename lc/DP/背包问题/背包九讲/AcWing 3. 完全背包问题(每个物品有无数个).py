"""
有 N 件物品和一个容量是 V 的背包。。

第 i 件物品的体积是 vi，价值是 wi。

相对于 01 背包，每个物品只能选一次
完全背包问题，我们每个物品都可以选无数次，我们要怎么做才能让一个容量上限，达到一个最大化
"""
# https://www.acwing.com/video/324/
def bagO2():
    N, V = map(int, input().split())

    # 为什么这里v,w第一个元素要放0，是因为下面for循环，我们遍历i是从1开始的
    # 因为不存在所谓的0号元素，所以我们统一把元素价值往后挪
    v = [0]  # 体积
    w = [0]  # 价值

    for i in range(N):
        comb = [int(i) for i in input().split()]
        v.append(comb[0])
        w.append(comb[1])

    # dp[i][j] 已选择物体的总体积<= i的条件下，从前j个物体中选，所能选出的最大价值
    dp = [[0] * (N + 1) for i in range(V + 1)]

    # 从前i个物体中选
    for i in range(1, N + 1):
        # 枚举容量
        for j in range(1, V + 1):
            # 相对与01背包，我们多了一个k，用于记录当前石头应该被选择多少次
            for k in range(0, j):

                # 我们不选择当前物品，所以dp[i][j] = dp[i-1][j]
                dp[i][j] = dp[i - 1][j]

                # 保证加入的K*石头不会超过容量
                if k * v[i] <= j:
                    # 我们不选择当前物品 * k个，所以dp[i][j] = dp[i-1][j - k * v[i]] + k*w[i]
                    # max表示从上面多种方案挑选出最优值
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - k * v[i]] + k * w[i])

    return dp[-1][-1]

"""
优化思路
我们列举一下更新次序的内部关系：

f[i , j ] = max( f[i-1,j] , f[i-1,j-v]+w ,  f[i-1,j-2*v]+2*w , f[i-1,j-3*v]+3*w , .....)
f[i , j-v]= max(            f[i-1,j-v]   ,  f[i-1,j-2*v] + w , f[i-1,j-2*v]+2*w , .....)
上式的很多状态比下式的状态多一个w

由上两式，可得出如下递推关系, 这样就已经把k给消掉了： 
                        f[i][j]=max(f[i-1][j], f[i,j-v]+w]) 

"""


def bagO2compressv1():
    N, V = map(int, input().split())

    v = [0]
    w = [0]

    for i in range(N):
        comb = [int(i) for i in input().split()]
        v.append(comb[0])
        w.append(comb[1])

    dp = [[0] * (V + 1) for j in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, V + 1):

            # 我们不选择当前物品，所以dp[i][j] = dp[i-1][j]
            dp[i][j] = dp[i - 1][j]

            # 我们选择当前物
            if v[i] <= j:
                # 我们知道dp[i][j] 和 dp[i][j-v[i]]是存在数学关系的，
                # 所以复用dp[i][j-v[i]] 的值就好了，减少了很多计算
                dp[i][j] = max(dp[i][j], dp[i][j - v[i]] + w[i])

    return dp[-1][-1]


"""
我们现在尝试把dp压缩至一维，从上面来看，我们除一段代码与01背包不一样以外，别的都是一样的

f[i][j] = max(f[i][j], f[i-1][j-v[i]] + w[i]); //01背包
f[i][j] = max(f[i][j], f[i]  [j-v[i]] + w[i]); //完全背包问题
"""

# 1D 完全背包
def bagO2compressv2():
    N, V = map(int, input().split())

    v = [0]
    w = [0]

    for i in range(N):
        comb = [int(i) for i in input().split()]
        v.append(comb[0])
        w.append(comb[1])

    dp = [0] * (V + 1)

    for i in range(1, N + 1):
        for j in range(0, V + 1):

            # 我们不选择当前物品，所以dp[i][j] = dp[i-1][j]
            # 这里消除i后，dp[j](这是修改后) = dp[j](这是修改前)
            # 这里i消除不对dp[j]造成影响，所以忽略

            if v[i] <= j:
                # 我们选择当前物品，所以dp[i][j] = dp[i][j - v[i]] + w[i]
                # 可以看到，左右两边都是dp[i]
                # 由于dp[i][j] 需要本轮的 dp[i][j - v[i]] 进行更新
                # 所以 dp[i][j - v[i]]的便利顺序得在 dp[i][j]之前，所以我们从小到大便利
                dp[j] = max(dp[j], dp[j - v[i]] + w[i])

    return dp[-1]


"""
我们怎么理解这两者的递推式都一样，但是只是j的执行顺序不同呢？
完全背包 dp[j]= max(dp[j], dp[j - v[i]]+ w[i])
01背包  dp[j] = max(dp[j], dp[j - v[i]] + w[i])

因为我们第一重循环定的是当前用的是哪个商品
从前往后的话，意味使用当前商品的状态可以进行复用，例如dp[6] = dp[4] + w[?] 这个dp[6] dp[4]是在同一个i下更新的
从后往前的话，意味着当前商品的状态是上一件物品决定的，例如dp[6] = dp[4] + w[?], 这个dp[4]是上一个商品的状态

重  价
1   2
2   4
3   4
4   5

我们发现，每次都选择了 重1价2的物品
[0, 2, 4, 6, 8, 10]
[0, 2, 4, 6, 8, 10]
[0, 2, 4, 6, 8, 10]
[0, 2, 4, 6, 8, 10]

"""
