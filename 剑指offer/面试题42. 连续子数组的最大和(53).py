class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # curSum记录的是当前子数组的最大值
        # maxSum记录的是全局的子数组最大值
        curSum = maxSum = nums[0]

        for num in nums[1:]:
            # 当之前 curSum已经小于0了，后面无论加入什么数字，都不会超过了比
            # 直接用那个数大
            if curSum <= 0:
                curSum = num
            # 当之前 curSum > 0, 那么我们继续加入后面的数字试试
            else:
                curSum += num

            # 记录，更改
            maxSum = max(maxSum, curSum)

        return maxSum