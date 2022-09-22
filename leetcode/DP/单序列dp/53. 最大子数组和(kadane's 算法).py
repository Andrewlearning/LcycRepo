import sys
class Solution(object):
    def FindGreatestSumOfSubArray(self, nums):
        res = -sys.maxsize
        curSum = 0

        for num in nums:
            # 把当前遍历到数字加入到序列和之中
            curSum = curSum + num

            # 看之前结果大, 还是当前结果大
            res = max(res, curSum)

            # 假如当前序列和 < 0的话，那么后面无论加什么数都会更小
            # 所以开始重新统计序列和
            if curSum < 0:
                curSum = 0

        return res

if __name__ == "__main__":
    solution = Solution()

"""
https://algocasts.io/episodes/deG4vW1R
Time: O(n), Space: O(1)

可以和leetcode 124对比着来看
"""