"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit.
Note: You may not engage in multiple transactions(交易) at the same time
（当天可以有无数次 买入 卖出）
 当天的买入卖出其实一样，不影响你的收益
"""

"""
本讲解来自灵神
https://www.bilibili.com/video/BV1ho4y1W7QK/?spm_id_from=333.880.my_history.page.click&vd_source=b81616a45fd239becaebfee25e0dbd35

定义 dfs(i,0)表示到第i天结束时，未持有股票的最大利润
定义 dfs(i,1)表示到第i天结束时，持有股票的最大利润

(重要)由于第i-1天的结束就是第i天的开始
则, max(dfs(i-1, 0 or 1)) 表示到第i天开始时的最大利润

第i天结束时,未持有股票的最大利润, dfs(i,0) = max(dfs(i-1,0), dfs(i-1,1) + prices[i])
第i天结束时，持有股票的最大利润,  dfs(i,1) = max(dfs(i-1,1), dfs(i-1,0) - prices[i])

递归边界:
dfs(-1,0) = 0, 第-1天的结束未持有股票 = 第0天开始未持有股票，利润为0
dfs(-1,1) = -inf, 第-1天的结束且持有股票 = 第0天开始不可能持有股票, 所以设置利润为-inf

递归入口:
max(dfs(n-1,0),dfs(n-1,1)), n-1表示最后一天，假如在最后一天你还持有股票，那么你的收益必然不可能最大
所以最后一天结束时的最大收益是未持有股票 -> dfs(n-1,0)

时间复杂度
- 状态的个数是n天 * 2(买，卖)，单个状态的计算时间O(1)，所以总体时间复杂度是O(n)
空间复杂度
- 由于有O(n)个状态，所以空间复杂度是O(n)
"""

# 这个的遍历顺序是从后往前，在遍历到最前的时候生成base case, 然后从前往后生成结果
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dfs(i, hold):
            # 递归边界
            # i = -1 case, 说明第0天开始
            if i < 0:
                # 第0天开始持有股票，不可能的情况，返回-inf
                if hold:
                    return -inf
                # 第0天开始没持有股票，利润为0，返回0
                else:
                    return 0

            # 第i天结束持有股票的最大值 = max(i-1天持有股票，i-1天未持有股票 + 第i天买入股票)
            if hold:
                return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i])
            # 第i天结束未持有股票的最大值 = max(i-1天未持有股票，i-1天持有股票 + 第i天卖出股票)
            else:
                return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])

        # 递归入口，最后一天结束且未持有股票
        return dfs(n - 1, False)

"""
翻译成递推
定义 dp[i][0] 表示到第i天结束时，未持有股票的最大利润
定义 dp[i][1] 表示到第i天结束时，持有股票的最大利润

由于在数组中无法表示用状态表示 f[-1][0]和 f[-1][1]
那就在f的最前面插入一个状态，dp状态数组总长度从 n -> n+1
所以
f[0][0] 表示到第0天开始时，未持有股票的最大利润
f[0][1] 表示到第0天开始时，持有股票的最大利润

f[i+1][0] 表示到第i+1天开始时/第i天结束时，未持有股票的最大利润
f[i+1][1] 表示到第i+1天开始时/第i天结束时，持有股票的最大利润

最终递推式
f[0][0]= 0
f[0][1]= -inf
f[i + 1][0] = max(f[i][0], f[i][1] + prices[i])
f[i + 1][1] = max(f[i][1], f[i][0] - prices[i])
答案为 f[n][0]
"""

# 这个的遍历顺序是从前往后，因为我们一开始知道了base case, 所以可以一直向后推导
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[0] * 2 for _ in range(n + 1)]

        # 初始状态
        # 第0天开始且持有股票是不可能的，所以是-inf
        # 第0天开始且不持有股票，是默认值0
        dp[0][1] = -inf

        for i, p in enumerate(prices):
            # 第i天结束持有股票的最大值 = max(i-1天持有股票，i-1天未持有股票 + 第i天买入股票)
            dp[i + 1][0] = max(dp[i][0], dp[i][1] + p)

            # 第i天结束未持有股票的最大值 = max(i-1天未持有股票，i-1天持有股票 + 第i天卖出股票)
            dp[i + 1][1] = max(dp[i][1], dp[i][0] - p)

        # 返回第n-1天结束且未持有股票的值(理论上的最大值)
        return dp[n][0]

"""
时间复杂度
- 状态的个数是n+1天 * 2(买，卖)，单个状态的计算时间O(1)，所以总体时间复杂度是O(n)
空间复杂度
- 数组大小为 2 * n+1，所以空间复杂度是O(n)
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        res = 0

        # 因为我们只能第一次卖出，产生收益，只能从第一天开始，因为是第0天买入
        for i in range(1,len(prices)):
            # 如果我们发现 今天的价格要比昨天的要高，那么我们就当买入昨天的，卖出今天的

            # 一个困惑点，这个算法如何思考[0,1,2,3,4]这种情况
            # 在i=1的时候，卖出股票，赚到1-0=1
            # 在i=2的时候，买入p=1的是股票，卖出p=2的股票，赚到2-1=1
            # 这样的计算方式相当于i=1的股票没卖
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]

        return res

"""
time: On space: O1
使用贪心的思路，只要后一天的价格>前一天，则进行买卖
"""