"""
问跳到数组最后最少需要几次
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
"""

#Time: O(n), Space: O(n)
def jump(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums is None or len(nums) == 0: return -1

    n = len(nums)
    next_max = 0
    step = [0] * n

    for i in xrange(n):
        if next_max >= n - 1: return step[n - 1]
        if i > next_max: return -1
        next_max = i + nums[i] if i + nums[i] > next_max else next_max
        last = next_max if next_max < n - 1 else n - 1
        for j in xrange(last, i, -1):
            if step[j] != 0:
                break
            step[j] = step[i] + 1

    return -1