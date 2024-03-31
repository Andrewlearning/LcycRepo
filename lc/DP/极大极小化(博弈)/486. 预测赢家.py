"""
给定一个表示分数的非负整数数组。 玩家1从数组任意一端拿取一个分数，随后玩家2继续从剩余数组任意一端拿取分数，然后玩家1拿，……。每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束。最终获得分数总和最多的玩家获胜。

给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。

示例 1:

输入: [1, 5, 2]
输出: False
解释: 一开始，玩家1可以从1和2中进行选择。
如果他选择2（或者1），那么玩家2可以从1（或者2）和5中进行选择。如果玩家2选择了5，那么玩家1则只剩下1（或者2）可选。
所以，玩家1的最终分数为 1 + 2 = 3，而玩家2为 5。
因此，玩家1永远不会成为赢家，返回 False。
"""


class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums and len(nums) == 0:
            return True

        length = len(nums)

        # dp[i][j] 表示 [i....j] 我方与对方的最大分差是多少(正数，且会轮流交换)
        dp = [[0] * length for _ in range(length)]

        # 初始化dp数组
        for i in range(length):
            dp[i][i] = nums[i]

        # 保证初始化的时候，至少留[i,j]两个位置
        for i in range(length - 2, -1, -1):
            for j in range(i, length, 1):
                # 当前我方和对方的最大分差是，我拿了nums[i]赚的，减去下一轮对方赚的
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

        # 因为玩家一第一个选，所以他拥有所有数字的选择权
        # 所以我们只要看dp[0-len] 是否大于0就可以了
        return dp[0][-1] >= 0

"""
time : O(N^2)
space : O(N)
https://leetcode-cn.com/problems/predict-the-winner/solution/dong-tai-gui-hua-python-by-jycoder-3/
"""