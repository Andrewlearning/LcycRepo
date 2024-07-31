class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 把不重复的元素，都通过这个指针来放置, k后面, 比如k-1...k-n都是按照要求的不重复区间
        # 我们只用判断，最新的元素(num) 和 不重复区最后两位的关系
        k = 0
        for num in nums:
            # k < 2, 前两位的数字不用考虑重复问题
            # nums[k-1] != num，例如2, 2(k-1)，这种情况，3是可以加入的
            # nums[k-2] != num，例如2, 2(k-2)，3(k-1)这种情况，num=3与[k-1]相等与[k-2]不等，是可以加入进去
            if k < 2 or nums[k-1] != num or nums[k-2] != num:
                nums[k] = num
                k += 1
        return k

