"""
给你一个 只包含正整数 的 非空 数组 nums。
请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11]
"""
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        total = sum(nums)

        # 总和不能刚好被平分成两份，所以不可能构成
        if total % 2 == 1:
            return False

        # 每一份数应该是1/2个total
        half = total // 2

        # dp[i][j] 从前i个数中选择，他们的目标和是否能达到j
        dp = [[False] * (half + 1) for i in range(len(nums))]

        # base case, 使用前i个数，目标和为0，只要所有的数都不去选择，那么就能满足和为0
        # 所以都为True
        for i in range(len(nums)):
            dp[i][0] = True

        # 枚举每个物品
        for i in range(1, len(nums)):
            # 枚举体积，从小到大
            for j in range(1, half + 1):
                # 假如不使用nums[i-1]这个元素，所以dp[i][j]的结果与dp[i-1][j]相同
                dp[i][j] = dp[i-1][j]

                # 假如使用nums[i-1]这个元素, 首先判断nums[i-1]会不会超出目标和
                # 假如没超出，我们则可以使用
                if j >= nums[i-1]:
                    dp[i][j] = dp[i-1][j - nums[i-1]] | dp[i][j]

        return dp[-1][-1]


"""
时间复杂度：O(NC)：这里 N是数组元素的个数, C 是数组元素的和的一半。
空间复杂度：O(NC)
古城算法: https://www.youtube.com/watch?v=ihf8JjQdta0 12:00
acwing较为详细的推导: https://www.acwing.com/video/944/
"""

# 压缩到一维，因为因为我们只会用到 dp[i] 和 dp[i-1]的状态
# 所以我们可以把i这一个纬度给去掉
class Solution(object):
    def canPartition1D(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        total = sum(nums)

        # 总和不能刚好被平分成两份，所以不可能构成
        if total % 2 == 1:
            return False

        # 每一份数应该是1/2个total
        half = total // 2

        # dp[i] 从已被遍历到的数的范围内进行选择，看被选择的数的和 是否能等于 i
        dp = [False] * (half + 1)

        # base case, 从所有数来选择，目标和为0，只要所有的数都不去选择，那么就能满足和为0
        # 所以都为1
        dp[0] = True

        # 枚举每个物品
        for i in range(len(nums)):
            # 从大到小枚举体积, 枚举范围[nums[i], half]
            for j in range(half, nums[i] - 1, -1):

                # 假如我们不使用nums[i], 那么dp[j] = dp[j], 所以我们可以省略
                # 假如我们使用nums[i], 那么dp[j] = dp[j - nums[i]]
                # |(or) 是表明我们从上面两种选法中取其中的最优解来记录
                dp[j] = dp[j - nums[i]] | dp[j]

        return dp[-1]

