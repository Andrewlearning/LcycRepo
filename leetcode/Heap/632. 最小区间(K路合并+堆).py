import heapq


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # [[i][j]的值, i, j]
        heap = []
        res = []
        maxValue = float("-inf")

        # 初始化小顶堆
        # 把每一列的第一个元素加进小顶堆。以及它的行列
        for i in range(0, len(nums)):
            heapq.heappush(heap, [nums[i][0], i, 0])
            # 更新初始的最大值
            maxValue = max(maxValue, nums[i][0])

        while len(heap):
            # 拿到堆中最小值
            top = heapq.heappop(heap)

            # 当前区间的最小值
            l = top[0]
            # 当前区间的最大值
            r = maxValue

            # 假如没有答案，或[l,r]区间比答案区间小
            if len(res) == 0 or res[1] - res[0] > r - l:
                res = [l, r]

            #  因为top[1][2]是当前堆的最小元素, 它已经被用了
            #  所以我们要把当前列的下一个元素给加进堆
            i = top[1]
            j = top[2] + 1
            if j < len(nums[i]):
                heapq.heappush(heap, [nums[i][j], i, j])
                maxValue = max(maxValue, nums[i][j])
            else:
                break

        return res


"""
https://www.acwing.com/video/2128/
本题是一个枚举。每次每一行上放一个指针。堆里记录每个指针
每次把堆里的最小元素找出来，然后再把堆里的最大元素找出来。这样【最小，最大】就能包含所有行的其中一个元素了
然后不断枚举，更新这个最小区间
"""