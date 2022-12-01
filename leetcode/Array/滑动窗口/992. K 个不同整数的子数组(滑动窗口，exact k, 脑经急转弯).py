"""
给定一个正整数数组 nums和一个整数 k，返回 num中 「好子数组」的数目。

如果 nums的某个子数组中不同整数的个数恰好为 k，则称 nums的这个连续、不一定不同的子数组为 「好子数组」。

例如，[1,2,3,1,2] 中有3个不同的整数：1，2，以及3。
子数组 是数组的 连续 部分。

示例 1：

输入：nums = [1,2,1,2,3], k = 2
输出：7
解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
示例 2：

输入：nums = [1,2,1,3,4], k = 3
输出：3
解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].。
"""
class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type A: List[int]
        :type k: int
        :rtype: int
        """
        # exact(k) = atMost(k) - atMost(k-1)
        return self.atMost(nums, k) - self.atMost(nums, k - 1)


    def atMost(self, nums, k):
        res = 0
        l = 0
        count = defaultdict(int)

        # r 作为滑动窗口的右边
        for r in range(len(nums)):

            # 假如说窗口新进来的数字出现的次数为0，k要-1
            # 因为这个新数字即将进入我们的滑动窗口了，要占掉k的一个份额
            if count[nums[r]] == 0:
                k -= 1
            count[nums[r]] += 1

            # 假如说k<0, 说明窗口内的不同数字数量太多了，我们要更新l来缩小滑动窗口
            while k < 0:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    k += 1
                l += 1

            # 以r为终点，从左往右收缩，产生子数组
            # [1,2,3], 以i=2为终点, i=0为起点，产生的子数组为
            # [1,2,3], [2,3], [3], 个数为2 - 0 + 1 = 3个
            # 我们记录的这个数字，则代表着滑动窗口中的数，能构成不同数字<=k个的子数组，个数为r - l + 1个
            res += r - l + 1

        return res

"""
https://www.bilibili.com/video/BV1Db411S751?from=search&seid=3091020131323956098
我们使用r - l + 1者种扫法，其实是能把所有的满足条件的子数组都扫出来的
[1,2,3]
i=0, [1]
i=1, [1,2] [2]
i=2, [1,2,3] [2,3] [3]
"""