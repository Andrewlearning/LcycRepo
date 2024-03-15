"""
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。

示例1:

输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
示例2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        self.nums = nums
        return self.dp(0)

    @cache
    def dp(self, cur):
        nums = self.nums

        # 假如当前下标已经到达或超过最后一位了，说明不能再走了，返回0
        if cur >= len(nums) - 1:
            return 0
        # 假如从当前下标出发，可以到达或超过最后一位了，说明可以再走一步，返回1
        if cur + nums[cur] >= len(nums) - 1:
            return 1

        # 我们在cur这个位置，最少可以走res步到最后一位
        res = float('inf')

        # 走1步 ~ nums[cur]步，因为走0步效果相同，就直接忽略了
        for i in range(1, nums[cur] + 1):
            # self.dp(cur + i)：从cur+i这个位置走，最少要走几步到终点
            # 每次记录最小的结果
            res = min(res, self.dp(cur + i) + 1)

        return res

"""
@cache的作用是，例如dp(0) return过一个结果，那么下次当调用到dp(0)的时候会返回上次获得的结果，不会重新计算
可以用@cache来作为一种dp的实现方式, 函数参数不能带有list, 因为无法被hash, 只能放int或string
只有python3才支持
用法解析: https://zhuanlan.zhihu.com/p/621769520

解题解析: https://www.youtube.com/watch?v=3mIc_mKP4yM
因为每次dp()里都有一个for循环，加上记忆化搜索需要计算每个节点，所以时间复杂度相当于O(n**2), 空间复杂度是O(n)
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
            # 假如说当前位置+ 当前位置能跳的最远距离 > 全程最大跳跃距离， 那么我们更新 全程最大跳跃距离
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
贪心做法，最优解
"""