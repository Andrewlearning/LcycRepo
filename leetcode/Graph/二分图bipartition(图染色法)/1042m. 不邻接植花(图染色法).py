"""
每个点可以有四种颜色的选择，只要两个相邻点的颜色不同就行

输入：n = 3, paths = [[1,2],[2,3],[3,1]]
输出：[1,2,3]
解释：
花园 1 和 2 花的种类不同。
花园 2 和 3 花的种类不同。
花园 3 和 1 花的种类不同。
因此，[1,2,3] 是一个满足题意的答案。其他满足题意的答案有 [1,2,4]、[1,4,2] 和 [3,2,1]
"""


class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * N
        neigh = [[] for _ in range(N)]
        
        # 每个点的相邻的点都记录起来
        for i, j in paths:
            neigh[i - 1].append(j - 1)
            neigh[j - 1].append(i - 1)

        for cur in range(N):
            # 当前i可以选择哪种花色
            flowers = [1, 2, 3, 4]
            for j in neigh[cur]:
                if res[j] in flowers:
                    flowers.remove(res[j])

            # 反正剩出来的都可以选，随意选
            res[cur] = flowers[0]

        return res