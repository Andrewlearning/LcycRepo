class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        for num in nums:
            # k < 2, 前两位的数字不用考虑重复问题
            # nums[k-1] != num，例如2，3这种情况，3是可以加入的
            # nums[k-2] != num，例如2，3，3这种情况，3与nums[k-1]相等与nums[k-2]不等，是可以加入进去
            if k < 2 or nums[k-1] != num or nums[k-2] != num:
                nums[k] = num
                k += 1
        return k

