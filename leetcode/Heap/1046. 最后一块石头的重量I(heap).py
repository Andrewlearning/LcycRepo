"""
有一堆石头，每块石头的重量都是正整数。
每一回合，从中选出两块 最重的 石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。
那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。

"""

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)

        while len(stones) >= 2:
            # 选出一个最重，和次重的石头
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)

            # 把他们碰到一起
            new = abs(s1 - s2)

            # 假如说石头没有消失，那么把它存进堆里
            if new != 0:
                heapq.heappush(stones, -new)

        # 假如说开局就两个[2,2]的石头，一碰就没了，所以要返回0
        # 否则则返回最后一颗石头的重量
        return 0 if len(stones) == 0 else -stones[0]

"""
Time: O(NlogN), 每个元素入堆调整logn, 共n个元素
Space: O(N)，堆的大小

https://leetcode-cn.com/problems/last-stone-weight/solution/shi-yong-you-xian-dui-lie-mo-ni-wen-ti-java-by-liw/
"""