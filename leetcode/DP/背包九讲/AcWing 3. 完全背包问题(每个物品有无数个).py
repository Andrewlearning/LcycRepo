"""

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

        # 从前i个物体中选，且已选择物体的总体积<= j，的最大价值
        dp = [[0] * (N + 1) for j in range(V + 1)]

        # 从前i个物体中选
        for i in range(1, N+1):
            # j代表容量
            for j in range(1, V+1):
                 # 相对与01背包，我们多了一个k，用于记录当前石头应该被选择多少次
                 for k in range(0, j):

                    dp[i][j] = dp[i-1][j]
                    # 保证加入的K*石头不会超过容量
                    if k*v[i] <= j:

                        dp[i][j] = max(dp[i][j], dp[i-1][j - k * v[i]] + k*w[i])

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

    dp = [[0 for i in range(V + 1)] for j in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, V + 1):

                dp[i][j] = dp[i - 1][j]
                # 复用上面的递推式，我们可以不需要k了
                if v[i] <= j:
                    # 我们知道dp[i][j] 和 dp[i][j-v[i]]是存在数学关系的，
                    # 所以复用dp[i][j-v[i]] 的值就好了，减少了很多计算
                    dp[i][j]= max(dp[i][j], dp[i][j - v[i]]+ w[i])

    return dp[-1][-1]

"""
以下有点难，可不尝试
我们现在尝试把问题压缩至一维，从上面来看，我们除一段代码与01背包不一样以外，别的都是一样的

f[i][j] = max(f[i][j], f[i-1][j-v[i]] + w[i]); //01背包

f[i][j] = max(f[i][j], f[i]  [j-v[i]] + w[i]); //完全背包问题

"""

def bagO2compressv2():
    N, V = map(int, input().split())

    v = [0]
    w = [0]

    for i in range(N):
        comb = [int(i) for i in input().split()]
        v.append(comb[0])
        w.append(comb[1])

    dp = [V for j in range(V + 1)]

    for i in range(1, N + 1):
        for j in range(0, V + 1):

                if v[i] <= j:
                    dp[j]= max(dp[j], dp[j - v[i]]+ w[i])

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