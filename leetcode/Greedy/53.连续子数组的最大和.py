import sys
class Solution(object):
    def FindGreatestSumOfSubArray(self, nums):
        res = -sys.maxsize
        sum = 0

        for num in nums:
            # 看重新开始收益大， 还是继续选择收益大
            sum = max(num, sum + num)

            # 看之前结果大, 还是当前结果大
            res = max(res, sum)

        return res

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