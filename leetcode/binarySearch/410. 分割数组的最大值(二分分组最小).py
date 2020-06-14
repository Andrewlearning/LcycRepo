"""
给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。

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
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        l = max(nums)
        r = sum(nums)
        length = len(nums)

        res = r

        while l <= r:
            # 区间和的最大值
            mid = (l + r) // 2
            # 区间和
            sub_sum = 0
            # 按照当前mid，总共能分几个区间
            count = 1

            for i in range(length):
                # 说明当前区间超过 我们想要分配的范围了
                if sub_sum + nums[i] > mid:
                    # 那么我们该找下一个区间了
                    count += 1
                    sub_sum = nums[i]
                else:
                    sub_sum += nums[i]

            # 假如说我们分配的区间数量，小于题目要求的数量，说明我们每个区间分配的数分多了
            # 那么我们要把下一次分配的最大值 缩小一下， r = mid - 1
            if count <= m:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res

# https://leetcode-cn.com/problems/split-array-largest-sum/solution/er-fen-cha-zhao-by-coder233-2/
# 讲解https://www.youtube.com/watch?v=_k-Jb4b7b_0