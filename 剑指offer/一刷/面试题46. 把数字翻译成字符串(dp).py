class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)

        dp = [1 for _ in range(len(s) + 1)]

        for i in range(2, len(s) + 1):
            # 我们可以选择翻译一位或者是两位
            if "10" <= s[i - 2:i] <= "25":
                dp[i] = dp[i - 1] + dp[i - 2]

            # 否则则是 01, 或者是 90这种情况，无法被两个元素被翻译
            # 所以只能翻译1位
            else:
                dp[i] = dp[i - 1]

        return dp[-1]

"""
https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/solution/mian-shi-ti-46-ba-shu-zi-fan-yi-cheng-zi-fu-chua-6/
time: O(N)
space: O(N)
"""