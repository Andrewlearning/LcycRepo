"""
有一堆石头，每块石头的重量都是正整数。

每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。

!! 最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。
"""
class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if not stones or len(stones) == 0:
            return 0


        total = sum(stones)

        half = total // 2

        dp = [0 for i in range(half + 1)]

        for stone in stones:
            for j in range(half, -1, -1):

                if j >= stone:
                    dp[j] = max(dp[j], dp[j - stone] + stone)

        return total - 2 * dp[-1]

"""
参考：https://www.cnblogs.com/19990219073x/p/10989013.html
时间：O(M * N)
空间：O(M)
M：石块总重；N：石块总数

本题是一道比较奇怪的01背包， 因为这题的背包容量是石头的重量， 价值也是石头的重量

然后我们要求相碰以后剩下石头的最小值，这个怎么理解
我们可以把所有的石头重量加起来， 然后尽可能均匀分成两堆，因为必然会有一堆重量大，一堆重量小
我们用dp求解 容量尽可能接近一半的石头堆的作用是 ————使那堆重量小的石头的重量尽可能的大
以至于，重量大的那堆重量尽可能小， 使得他们的差值达到一个最小的状态

然后最后, 因为我们真不能确定high的值是多大，所以这里利用了一种的计算方法
total = high + low
所以 total - 2*dp[-1] = (high + low) - 2*low = high - low = 我们想要的答案
"""