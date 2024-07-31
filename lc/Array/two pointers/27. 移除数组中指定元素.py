"""
题目主要意思就是，把不用删除的数字都放到前面，把要删除的数字放到后面，最后返回
除去删除后剩下几个数字

 nums = [0,1,2,2,3,0,4,2], val = 2

 返回5，说明只有5个数字是非val的，而且要求nums前5位都是非val的数字，要求inplace
Output: 5, nums = [0,1,4,0,3,_,_,_]
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return

        slow = 0

        for fast in range(len(nums)):
            # 如果fast不等于我们要移除的元素，那么就把fast填充到
            # slow里面去，然后让slow++
            # 目的是使得slow左边的都是非目标元素
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

        return slow

"""
Time: O(n), Space: O(1)
https://algocasts.io/episodes/AwmX8Jmx
"""

