"""
传送带上的包裹必须在 D 天内从一个港口运送到另一个港口。

传送带上的第 i 个包裹的重量为 weights[i]。每一天，我们都会按给出重量的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。

返回能在 D 天内将传送带上的所有包裹送达的船的最低运载能力。

 

示例 1：

输入：weights = [1,2,3,4,5,6,7,8,9,10], D = 5
输出：15
解释：
船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10

请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。
"""


class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        # 左闭右闭区间
        # 而最小、最大的运载能力分别为max(weights), sum(weights)
        l = max(weights)
        r = sum(weights)

        while l <= r:
            mid = (l + r) // 2
            # 能提前完成任务，说明负担加的太重，要减轻
            if D >= self.needDay(weights, mid):
                r = mid - 1
            else:
                l = mid + 1

        # 求得是能完成任务前提下的最轻重量，所以是最左有效边界
        return l

    def needDay(self, weights, capacity):
        count = 0
        curweight = 0
        for i in range(len(weights)):
            curweight += weights[i]
            if curweight > capacity:
                curweight = weights[i]
                count += 1

        # 当还有剩余的话，那么也要单独再运一次
        return count + int(curweight > 0)