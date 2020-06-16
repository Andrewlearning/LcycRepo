class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sets = set(nums)
        res = 0


        while sets:

            # 当集合中还有元素的时候，我们就不断的pop元素出来，然后检查他的扩散是否在sets里面
            num = sets.pop()

            # (low,high)
            low = num - 1
            high = num + 1

            # 我们以low, 和high向两边扩散，使得可以产生一个连续的下标
            while low in sets:
                sets.remove(low)
                low -= 1

            while high in sets:
                sets.remove(high)
                high += 1

            # 计算长度
            res = max(res, high - low - 1)

        return res

"""
Time O(n) Space: O(n)
https://algocasts.io/episodes/AEpo1MmQ
"""