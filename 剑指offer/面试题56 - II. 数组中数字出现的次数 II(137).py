"""
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

 

示例 1：

输入：nums = [3,4,3,3]
输出：4
示例 2：

输入：nums = [9,1,7,9,7,9,7]
输出：1
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        res = 0

        for bit in range(32):
            cur_sum = 0
            for num in nums:
                cur_sum += (num >> bit) & 1

            if cur_sum % 3 == 1:
                res |= (1 << bit)

        return self.convert(res)

    def convert(self, num):
        if num >= 2 ** 31:
            num -= 2 ** 31

        return num

"""
# lc 137
"""