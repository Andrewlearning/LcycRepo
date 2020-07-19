"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
    [2],
    [3,4],
    [6,5,7],
    [4,1,8,3]
]

"""


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle and len(triangle):
            return 0

        # res用最长的那个子数组，保证不会越界
        res = triangle[-1]

        # 从倒数第二层向上走
        for i in range(len(res) - 2, -1, -1):
            for j in range(len(triangle[i])):
                # 从下往上
                # 当前位置的值triangle[j] + 下一层相邻的最小值min(res[j], res[j+1])
                res[j] = triangle[i][j] + min(res[j], res[j + 1])

        return res[0]

