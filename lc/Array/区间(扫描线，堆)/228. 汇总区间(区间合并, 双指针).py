"""
Given a sorted integer array without duplicates, return the summary of its ranges.
Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
就是相连的数用x->y append到res里
"""
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums or len(nums) == 0:
            return []

        res = []
        # l,r代表一个组合的左右边界
        l = 0
        r = 0
        while r < len(nums):
            # 新开始一个区间
            l = r

            # 假如存在连续的数，那么r一直移动到没有连续的数为止
            while r + 1 < len(nums) and nums[r] + 1 == nums[r+1]:
                r += 1

            # 结束扩散后
            # 假如说发现没有扩散，那么说明没有连续的数，把当前数加进去
            if l == r:
                res.append(str(nums[l]))
            # 假如有扩散，那我们合并加进去
            else:
                res.append(str(nums[l]) + "->" + str(nums[r]))

            # 当前区间已经记录完成，跳到下一个区间继续
            r += 1

        return res

# 163
# https://leetcode-cn.com/problems/summary-ranges/solution/hui-zong-qu-jian-by-leetcode/