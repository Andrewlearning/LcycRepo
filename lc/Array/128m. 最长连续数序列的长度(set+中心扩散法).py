"""
Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
我们只要找到数组中存在最长连续数字是多长，不用在乎是否连在一起
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 用hashmap是为了查询key在不在里面的时间复杂度为O(1)
        m = {}
        for num in nums:
            m[num] = 1

        res = 0

        for num in nums:
            if num in m:
                # 当集合中还有元素的时候，我们就不断的pop元素出来，然后检查他的扩散是否在sets里面
                del m[num]

                # (l,r)
                l = num
                r = num

                # 我们以l, 和r向两边扩散，使得可以产生一个连续的下标
                while l - 1 in m:
                    l -= 1
                    del m[l]

                while r + 1 in m:
                    r += 1
                    del m[r]

                # 计算长度
                res = max(res, r - l + 1)

        return res

"""
Time O(n) Space: O(n)
https://algocasts.io/episodes/AEpo1MmQ
"""