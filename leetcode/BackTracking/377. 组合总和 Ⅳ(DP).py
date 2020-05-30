"""
给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。

示例:

nums = [1, 2, 3]
target = 4

所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
请注意，顺序不同的序列被视作不同的组合。
"""


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # 建立一个递推数组， 从值0 - 值target
        # 每个值所对应的是，构成这个值能有多少种方法
        dp = [0 for i in range(target + 1)]

        # 任何数的方法数 当碰到与自己相等的数的时候，都为1， 例如目标是2 ，碰到一个数是2，方法数为1
        dp[0] = 1

        for i in range(target + 1):
            for value in nums:
                # 当当前数字 已经超过我们要求的目标值的时候，跳过
                if value > i:
                    continue

                # 否则，构成数字i 的方法， 是有构成数字 [i-value]的方法
                # 相加得来的

                dp[i] += dp[i - value]

        return dp[-1]

"""
这题用回溯法会超时

https://www.youtube.com/watch?v=yNq7JFd7sHE&t=81s
Where n is length of nums and m is target,
Time complexity: O(nm)
Space complexity: O(m)
"""