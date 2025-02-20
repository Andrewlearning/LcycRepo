"""
问跳到数组最后最少需要几次
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dp(cur):
            # 假如当前下标已经到达或超过最后一位了，说明不能再走了，返回0
            if cur >= n - 1:
                return 0
            # 假如从当前下标出发，可以到达或超过最后一位了，说明可以再走一步，返回1
            if cur + nums[cur] >= n-1:
                return 1

            # 我们在cur这个位置，最少可以走res步到最后一位
            res = float('inf')

            # 走1步 ~ nums[cur]步，因为走0步效果相同，就直接忽略了
            for i in range(1, nums[cur] + 1):
                # self.dp(cur + i)：从cur+i这个位置走，最少要走几步到终点
                # 每次记录最小的结果
                res = min(res, self.dp(cur + i) + 1)
            return res

        return dp(0)

"""
@cache的作用是，例如dp(0) return过一个结果，那么下次当调用到dp(0)的时候会返回上次获得的结果，不会重新计算
可以用@cache来作为一种dp的实现方式, 函数参数不能带有list, 因为无法被hash, 只能放int或string
只有python3才支持
用法解析: https://zhuanlan.zhihu.com/p/621769520

解题解析: https://www.youtube.com/watch?v=3mIc_mKP4yM
因为每次dp()里都有一个for循环，加上记忆化搜索需要计算每个节点，所以时间复杂度相当于O(n**2), 空间复杂度是O(n)
"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None and len(nums) == 0:
            return -1

        if len(nums) == 1:
            return 0

        n = len(nums)

        # 再跳一次的话，能跳的最远距离
        next_max = 0

        # 在当前跳跃的次数里，能跳到的最远距离
        cur_max = 0

        # 已经跳跃的次数
        jump = 0


        for i in range(n):
            # 假如说我们再跳一次的话，可以到达或者超越终点，那么我们返回当前的跳跃次数+1
            if next_max >= n-1:
                return jump + 1

            # 假如走到一个下标， 是我们再跳一次也达不到的
            # 那么说明到达不了这个下标 -> 我们也更跳不到终点
            if i > next_max:
                return -1

            # 假如到了一个下标，已经到我们当前跳跃次数的极限了
            # 那么说明我们要再跳一次
            if i > cur_max:
                jump += 1
                cur_max = next_max

            # 下一次的跳跃最大距离
            next_max = max(next_max, i+nums[i])

        return -1

"""
https://algocasts.io/episodesaAEpo1vmQ
Time: O(n), Space: O(1)
贪心做法，最优解
"""