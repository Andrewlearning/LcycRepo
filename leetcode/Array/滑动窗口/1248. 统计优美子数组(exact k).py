"""
给你一个整数数组nums 和一个整数 k。如果某个连续子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
请返回这个数组中 「优美子数组」 的数目。

示例 1：

输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
示例 2：

输入：nums = [2,4,6], k = 1
输出：0
解释：数列中不包含任何奇数，所以不存在优美子数组。
"""
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 奇数个数<=k的子数组数量 - 奇数个数<=k-1的子数组数量 = 奇数个数=k子数组数量
        return self.atMost(nums, k) - self.atMost(nums, k - 1)

    def atMost(self, nums, k):
        res = 0
        left = 0
        # 记录滑动窗口内部有多少个奇数
        count = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                count += 1

            while count > k:
                if nums[left] % 2 == 1:
                    count -= 1
                left += 1

            # 统计滑动窗口内，能构成 奇数个数<=k的子数组数量
            res += i - left + 1
        return res

"""
参考992
"""