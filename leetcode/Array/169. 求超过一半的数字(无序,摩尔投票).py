"""
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。


"""
class Solution(object):
    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None and len(nums) == 0:
            return 0

        res = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if count == 0:
                res = nums[i]
                count = 1

            elif res == nums[i]:
                count += 1
            else:
                count -= 1

        return res


"""
https://algocasts.io/episodes/VlWd8W06
摩尔投票法
时间 O(n),空间O(1)
我们用res 来记录当前数量最多的数字
我们用count 来记录当前res记录的数字出现的次数，
遇到相同的数字，count 就加一， 遇到不相同的数字，count就-1
  nums[i] == res: count ++
  nums[i] != res: count --
  if count == 0:
        res = nums[i]
        count = 1
    
"""