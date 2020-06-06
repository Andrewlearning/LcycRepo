"""
问跳到数组最后最少需要几次
"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return False

        if len(nums) == 1:
            return 0

        n = len(nums)

        # 再跳一次的话，能跳的最远距离
        maxindex = 0

        # 在当前跳跃的次数里，能跳到的最远距离
        curEnd = 0

        # 已经跳跃的次数
        jump = 0


        for i in range(n):
            # 假如说我们再跳一次的话，可以到达或者超越终点，那么我们返回当前的跳跃次数+1
            if maxindex >= n-1:
                return jump + 1

            # 假如走到一个下标， 是我们再跳一次也达不到的
            # 那么说明到达不了这个下标 -> 我们也更跳不到终点
            if i > maxindex:
                return -1

            # 假如到了一个下标，已经到我们当前跳跃次数的极限了
            # 那么说明我们要再跳一次
            if i > curEnd:
                jump += 1
                curEnd = maxindex

            # 下一次的跳跃最大距离
            maxindex = max(maxindex,i+nums[i])

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
    maxindex = 0
    step = [0] * n

    for i in xrange(n):
        if maxindex >= n - 1: return step[n - 1]
        if i > maxindex: return -1
        maxindex = i + nums[i] if i + nums[i] > maxindex else maxindex
        last = maxindex if maxindex < n - 1 else n - 1
        for j in xrange(last, i, -1):
            if step[j] != 0:
                break
            step[j] = step[i] + 1

    return -1