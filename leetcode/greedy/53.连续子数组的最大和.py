import sys
class Solution(object):
    # 1
    def FindGreatestSumOfSubArray(self, nums):
        res = -sys.maxsize
        sum = 0

        for num in nums:
            sum = max(num, sum + num)
            res = max(res, sum)

        return res

    # 2
    def maxSubArray(self, array):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 我们为什么一开始不把sum 定成0呢？
        # 因为我们的测试条件中有可能会出现，[-5,-1,-2]这种情况
        cursum = maxsum = array[0]
        for i in array[1:]:
            if cursum <= 0:
                cursum = i
            else:
                cursum += i

            # 假如在出现[-5,-1,-2]这种情况，我们对比的是，前面的序列和小点，还是当前index小点
            # 就是虽然两种情况都很烂，但是还是可以比较一下
            maxsum = max(cursum, maxsum)
        return maxsum

if __name__ == "__main__":
    solution = Solution()

"""
https://algocasts.io/episodes/deG4vW1R
Time: O(n), Space: O(1)
对应leetcode 53.maximun subarray
原理非常简单暴力，关键在 cursum = max(i, cursum + i)，看看加上
下一个数是不是与 直接用下一个数 ，哪个比较大


2.可以和leetcode 124对比着来看
"""