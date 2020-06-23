"""
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
Example:
Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
"""
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """

        # 这个是根据测试案例来的，最后一个元素有个区间要到upper
        nums.append(upper + 1)

        res = []

        # low要等于lower-1, 因为它肩负着
        low = lower - 1
        for num in nums:
            # 看nums[i] ~ nums[i-1]的区间有多大
            diff = num - low

            # low = 1, num = 3, 结果"2"
            if diff == 2:
                res.append(str(low + 1))
            # low = 3, num = 50 结果"4 -> 50"
            if diff > 2:
                res.append(str(low + 1) + "->" + str(num - 1))

            # 每次循环更新low = num
            low = num

        return res


"""
https://leetcode-cn.com/problems/missing-ranges/solution/missing-ranges-shuang-zhi-zhen-fa-by-jyd/
感觉跟228summary range很像
https://www.youtube.com/watch?v=Cb_67muiXmo
"""