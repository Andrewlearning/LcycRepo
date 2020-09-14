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

            # (l,r)
            l = num
            r = num

            # 我们以l, 和r向两边扩散，使得可以产生一个连续的下标
            while l - 1 in nums:
                l -= 1
                nums.remove(l)

            while r + 1 in nums:
                r += 1
                nums.remove(r)

            # 计算长度
            while r + 1 in nums:
                r += 1
                nums.remove(r)

        return res

"""
Time O(n) Space: O(n)
https://algocasts.io/episodes/AEpo1MmQ
"""