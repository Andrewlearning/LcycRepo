"""
nums = [1, 7, 3, 6, 5, 6]
输出: 3
解释:
索引3 (nums[3] = 6) 的左侧数之和(1 + 7 + 3 = 11)，与右侧数之和(5 + 6 = 11)相等。
同时, 3 也是第一个符合要求的中心索引。
"""

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return -1

        n = len(nums)

        # 因为我们有n个数字， 例如 1 2, 这个数组其实有三个前缀和 x1 1 x2 2 x3
        # 所以这里presum的长度是n+1
        preSum = [0] * (n + 1)

        # 每一个前缀和的构成要严格满足下面条件，index = 0因为前面没有数，所以不做处理
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]

        # 假如 [0,i-1] ==  [i-n] ([0-n] - [0-i])
        # 那么说明index i就是平衡点
        for i in range(n):
            if preSum[i] == preSum[n] - preSum[i + 1]:
                return i

        return -1

"""
Time: O(n), Space: O(n)
https://algocasts.io/episodes/8eGx0zGM
"""
