"""
给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。
（使得每个子数组的大小最平均）

输入:
nums = [7,2,5,10,8]
m = 2

输出:
18

解释:
一共有四种方法将nums分割为2个子数组。
其中最好的方式是将其分为[7,2,5] 和 [10,8]，
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
"""

class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        l = max(nums)

        # 每个分组的最大和，就是一个数组总和
        r = sum(nums)

        while l < r:
            # mid, 是我们设定区间和的最大值
            mid = (l + r) // 2

            # 我们希望分组的数量 <= k的最大值，既是右边界(为啥是这样处理呢？为什么不是找左边界呢)
            # 假如说我们分配的区间数量，<= 题目要求的数量，说明我们每个区间分配的和分多了
            # 那么我们要把下一次分配的最大值 缩小一下， r = mid
            if self.countGroup(nums, mid) <= k:
                r = mid
            # 假如count 太多，说明我们把和分的太小了，要让分组的和高一点
            else:
                l = mid + 1

        return r

    # 计算以mid为分组和的最大值，最多能分k组吗？
    def countGroup(self, nums, mid):
        # 按照当前mid，总共能分几个区间
        count = 0

        # 当前区间的和
        sub_sum = 0

        for num in nums:
            sub_sum += num

            # 和超过mid的话，那么nums[i]则不算进上一个区间内，它将单独将作为一个新区间重新开始
            if sub_sum > mid:
                # 那么我们该找下一个区间了，区间数+1
                count += 1
                sub_sum = num

        # 处理最后一个分组
        if sub_sum > 0:
            count += 1

        return count

# https://leetcode-cn.com/problems/split-array-largest-sum/solution/er-fen-cha-zhao-by-coder233-2/
# 讲解https://www.youtube.com/watch?v=_k-Jb4b7b_0