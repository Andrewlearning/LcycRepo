"""
有一排房子给你抢劫，但是有个规则就是你不能连续抢两个房子，同时你不能同时抢首尾两个house，问你最多能抢多少钱
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)

        # 因为收尾并不能同时收割
        # 所以我们选择不走头，或者不走尾， 这样就能保证代码是可以的
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    # 这里用的就是第一题的源代码
    def helper(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]

"""
答案：
1.因为多了一个首尾房子不能同时抢的规定，其他的与上一题一样
2.所以我只要把首尾给分开成两次来求，看哪个片段比较大就好了
3.时间复杂度和空间复杂度与上题一样
"""