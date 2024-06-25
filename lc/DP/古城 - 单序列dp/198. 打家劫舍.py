"""
有一排房子给你抢劫，但是有个规则就是你不能连续抢两个房子，问你最多能抢多少钱
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""
# Time: O(n), Space: O(n)
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n

        if n <= 2:
            return max(nums)

        # 没有选择的时候，抢当前房子肯定是收益最大
        dp[0] = nums[0]

        # 当我们0，1可以选择的时候，我们肯定抢0，1中最大的那个
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):

            # 我们可以选择抢当前的房子，所以就不能抢上一家房子
            # dp[i] = nums[i] + dp[i-2]
            # 我么可以选择不抢当前的房子，所以当前的值沿用上一家的值
            # dp[i] = nums[i-1]
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]

# Time: O(n), Space: O(1)
class Solution1(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0: return 0
        prev1 = 0
        prev2 = 0

        for num in nums:
            cur = max(prev1 , prev2 + num)
            prev2 = prev1
            prev1 = cur
        return prev1


