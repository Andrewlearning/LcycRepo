class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        n = len(nums)
        left = 0

        # 维持一个在[l,r]范围内 [0]最大的递减单调队列
        maxd = []
        # 维持一个在[l,r]范围内 [0]最大的递减单调队列
        mind = []

        res = 0

        for r in range(n):
            # 假如发现前一个数比当前数小，那么把递减队列的前一个数干掉
            while maxd and maxd[-1] < nums[r]:
                maxd.pop(-1)

            # 假如发现前一个数比当前数小，那么把递减队列的前一个数干掉
            while mind and mind[-1] > nums[r]:
                mind.pop(-1)

            maxd.append(nums[r])
            mind.append(nums[r])

            # 假如两个极值的单调队列的差不符合我们的需求
            # 那么我们需要调整这两个单调队列
            # TODO 为什么这里这样处理
            if maxd[0] - mind[0] > limit:
                if maxd[0] == nums[left]:
                    maxd.pop(0)
                if mind[0] == nums[left]:
                    mind.pop(0)
                left += 1

            res = max(res, r - left + 1)

        return res

# https://www.youtube.com/watch?v=TA8S1UHI8W0 45:00
# 维护区间的 一个递增队列，一个递减队列，然后他们的队首元素分别是当前区间的最大值和最小值，他们的差就是题目要求的limit
# 当满足条件的时候，记录左右区间的下标差值