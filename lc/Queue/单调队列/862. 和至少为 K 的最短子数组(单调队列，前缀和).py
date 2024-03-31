"""
给你一个整数数组 nums 和一个整数 k ，找出 nums 中和至少为 k 的 最短非空子数组
，并返回该子数组的长度。如果不存在这样的 子数组 ，返回 -1 。

子数组 是数组中 连续 的一部分。
"""

class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        preSum = [0] * (n + 1)
        preSum[0] = nums[0]

        # 构造前缀和
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]


        deque = [0]
        res = float("inf")
        # 需求: i < j && preSum[j] - preSum[i] >= k && (j - i)最小
        # 通俗理解是，相当于排队，对某个人来说，要找到前面比我矮最少k的人，且我和那个人的距离最近
        for i in range(n + 1):
            # 当有满足条件的前缀和时，我们把他们pop出来
            # 同时更新最优答案
            while deque and preSum[i] - preSum[deque[0]] >= k:
                res = min(i - deque[0], res)
                deque.pop(0)

            # 这种情况就是相当于排队，前面一个人比我高，那就应该把前面比我高的人给干掉
            # 要不然的出来的前缀和一定是负数，这里有贪心的成分，难以证明为什么这样就是最优
            while deque and preSum[deque[-1]] >= preSum[i]:
                deque.pop(-1)

            deque.append(i)

        # 假如不存在答案，返回-1
        if res == float("inf"):
            return -1
        return res

"""
古城做法和acwing一样，30:37
https://www.youtube.com/watch?v=TA8S1UHI8W0
"""