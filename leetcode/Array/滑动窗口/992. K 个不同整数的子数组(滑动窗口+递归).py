class Solution(object):
    def subarraysWithKDistinct(self, nums, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # 这里比较巧妙，helper记录的是 <= K 的所有子串， 所以我们这样一减，得到我们想要的结果
        return self.helper(nums, K) - self.helper(nums, K - 1)

    def helper(self, nums, K):
        res = 0
        l = 0
        # 题目规定 1 <= A[i] <= A.length， count用来记录nums里面的每个数字出现的次数
        # 例如[1,2,1,2] 对应 count = [0,2,2,0]
        count = [0] * (len(nums) + 1)

        # r 作为滑动窗口的右边
        for r in range(len(nums)):

            # 假如说窗口新进来的数字出现的次数为0，k要-1
            # 因为这个新数字即将进入我们的滑动窗口了，要占掉k的一个份额
            if count[nums[r]] == 0:
                K -= 1

            # 判断完后才在count里更新
            count[nums[r]] += 1


            # 假如说k<0, 说明窗口内的不同数字数量太多了，我们要更新l来缩小滑动窗口
            while K < 0:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    K += 1
                l += 1

            # nums = [1,2,1,2,3]，K = 2, 那么l = 0, r = 3是满足要求的，0-3 [1,2,1,2]
            # 然后[1,2,1,2] 可以变为当K <= 2时，有多少k个不同整数的子序列，[1,2,1,2][2,1,2][1,2][2]四个
            # 所以这里统一用res 来记录当 K <= x的结果，后续用相减来去掉
            res += (r - l + 1)

        return res

"""
https://www.bilibili.com/video/BV1Db411S751?from=search&seid=3091020131323956098
16分钟开始
一切操作，都要注意好逻辑顺序，要不然很容易出错
"""