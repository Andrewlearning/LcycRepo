"""
有一堆石头，每块石头的重量都是正整数。

每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为x 和y，且x <= y。那么粉碎的可能结果如下：

如果x == y，那么两块石头都会被完全粉碎；
如果x != y，那么重量为x的石头将会完全粉碎，而重量为y的石头新重量为y-x。

最后，最多只会剩下一块石头。返回此石头最小的可能重量。如果没有石头剩下，就返回 0。
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

        # dp[i] 从已被遍历到的stone的范围内进行选择，看被选择的石头重量的和 是否能等于i
        dp = [0] * (half + 1)

        # 枚举每个物品
        for stone in stones:
            # 枚举体积，从大到小，1D模板
            for j in range(half, stone - 1, -1):
                # 假如我们不使用stone, 那么dp[j] = dp[j], 所以我们可以省略
                # 假如我们使用stone, 那么dp[j] = dp[j - stone]
                # max 是表明我们从上面两种选法中取其中的最优解来记录
                dp[j] = max(dp[j], dp[j - stone] + stone)

        return total - 2 * dp[-1]

"""
参考：https://www.youtube.com/watch?v=ihf8JjQdta0
时间：O(len(stones) * half)
空间：O(len(stones))

本题是一道比较奇怪的01背包， 因为这题的背包容量是石头的重量， 价值也是石头的重量

然后我们要求相碰以后剩下石头的最小值，这个怎么理解
我们可以把所有的石头重量加起来， 然后尽可能均匀分成两堆，因为必然会有一堆重量大，一堆重量小
我们用dp求解 容量尽可能接近一半的石头堆的作用是 ————使那堆重量小的石头的重量尽可能的大
以至于，重量大的那堆重量尽可能小， 使得他们的差值达到一个最小的状态

然后最后, 因为我们真不能确定high的值是多大，所以这里利用了一种的计算方法
total = high + low
所以 total - 2*dp[-1] = (high + low) - 2*low = high - low = 我们想要的答案
"""