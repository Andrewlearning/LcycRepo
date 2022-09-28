"""
Given a t, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following t

[
    [2],
    [3,4],
    [6,5,7],
    [4,1,8,3]
]

"""


class Solution(object):
    def minimumTotal(self, t):
        """
        :type t: List[List[int]]
        :rtype: int
        """
        if not t and len(t):
            return 0

        # 从倒数第二层向上走
        for i in range(len(t) - 2, -1, -1):
            for j in range(len(t[i])):
                # 从下往上求最小值
                # 当前位置[i][j]的和最小值 = t[i][j] + 下一层相邻的最小值min(t[i+1][j], t[i+1][j+1])
                # 从上往下求比较麻烦，数组容易越界
                t[i][j] += min(t[i+1][j], t[i+1][j + 1])

        return t[0][0]

"""
https://www.acwing.com/video/1475/
2
3,4
(6),5,7
(4),(1),8,3

我们可以看到，每一个[i][j] 是和 下一层[i+1][j] [i+1][j+1]相邻的
"""