"""
Given an array nums, there is a sliding window of size k which is moving
from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position. Return the max sliding window.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 双端单调队列，从前 -> 后，大 -> 小
        # 我们始终保持队列头元素是最大的
        # 存的是元素下标
        deque = []
        res = []
        n = len(nums)

        for i in range(n):
            # 当deque的首元素下标，已经超过我们滑动窗口的区间时，应该不纳入我们的考虑范围
            while deque and deque[0] < i - k + 1:
                deque.pop(0)

            # 当前遍历到元素 > 队列末尾元素时，需要把比nums[i]小的去掉
            # 这样去保持单调队列的单调性
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop(-1)

            # 处理完后把当前元素加入到deque中
            deque.append(i)

            # 当第一个区间已经填满时，意味我们可以开始记录区间的最大值了
            # 区间的最大值永远是队列头元素
            if i >= k - 1:
                res.append(nums[deque[0]])

        return res


"""
https://www.acwing.com/activity/content/problem/content/2633/
time O(n) space O(n)
单调队列模板题
需要维护一个大->小，长度为k的单调队列，每次记录队首元素作为答案
"""



