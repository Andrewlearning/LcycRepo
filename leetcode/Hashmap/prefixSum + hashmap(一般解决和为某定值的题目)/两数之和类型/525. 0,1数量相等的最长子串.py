"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
给一个binary数组，找出最长的子数组，0，1数量相等

链接：https://www.jianshu.com/p/7108226dc023
"""
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 先把所有的0变成-1
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1

        # key=curSum的值
        # value=当前子串的最后一位下标
        hashmap = {}
        hashmap[0] = -1
        curSum = 0
        res = 0

        for i in range(len(nums)):
            curSum += nums[i]

            # 当两个子串的差为0的时候，说明中间这一段0和1的数量是相等的，记录长度
            if curSum in hashmap:
                res = max(res, i - hashmap[curSum])
            # 若不存在，则记录当前curSum
            else:
                hashmap[curSum] = i

        return res

"""
古城算法 24:20
https://www.bilibili.com/video/BV1xB4y1N7Ut/?spm_id_from=333.999.0.0&vd_source=b81616a45fd239becaebfee25e0dbd35

相同的的两个sum出现后证明subarray部分的sum=0, 这时候因为只有1和-1，所以我们确定1和-1的数量的相同的
"""