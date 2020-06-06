"""
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        maxjump = 0
        terminal = len(nums) - 1

        for i in range(len(nums)):
            #我们的行动范围不能大于 最大跳跃距离，如果超过了就错了
            if i > maxjump:
                break
            # 假如说当前位置+能跳的距离 大于 最大跳跃距离， 那么我们更新最大跳跃距离
            if i + nums[i] > maxjump:
                maxjump = i + nums[i]

            # 假如我们最大跳跃距离 >= 最后的位置，说明我们可以完成任务
            if maxjump >= terminal:
                return True

        #假如我们所有步骤都走完了，还是没有完成任务，说明完不成任务
        return False

"""
Time: O(n), Space: O(1)
1.我们知道，我们能跳到的最远的距离是 curindex + nums[curindex]
  所以我们只需要判断，我们在数组中找到的最大curindex + nums[curindex]
  是否 >= len(nums)-1即可
2.同时我们得保证 curindex是在maxindex的活动范围以内的
"""