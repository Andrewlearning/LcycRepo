"""
给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。

请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。工人的 工作时间 是完成分配给他们的所有工作花费时间的总和。请你设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。

返回分配方案中尽可能 最小 的 最大工作时间 。

示例 1：

输入：jobs = [3,2,3], k = 3
输出：3
解释：给每位工人分配一项工作，最大工作时间是 3 。
示例 2：

输入：jobs = [1,2,4,7,8], k = 2
输出：11
解释：按下述方式分配工作：
1 号工人：1、2、8（工作时间 = 1 + 2 + 8 = 11）
2 号工人：4、7（工作时间 = 4 + 7 = 11）
最大工作时间是 11 。
"""

class Solution(object):
    def minimumTimeRequired(self, jobs, k):
        """
        :type jobs: List[int]
        :type k: int
        :rtype: int
        """
        self.res = float('inf')

        # 把job的排序，从小到大排
        jobs.sort()

        # 从大的job开始分配
        self.dfs(jobs, len(jobs) - 1, [0] * k)
        return self.res

    def dfs(self, jobs, pos, tSum):
        # 假如所有的工作都已经分配完了，那么看看在这种分配方法，和之前已有的结果相比，哪种更好一点
        if pos < 0:
            self.res = min(self.res, max(tSum))
            return

        # 假如当前某一worker的时间已经比之前结果差了，剪枝
        if max(tSum) >= self.res:
            return

        # 把当前工作分配给worker
        for i in range(len(tSum)):

            # 一个工作分配给几个worker是相同效果的话，我们就只分配给第一个woker就好了，都分配的话因为增加无效遍历，剪枝
            if i > 0 and tSum[i] == tSum[i - 1]:
                continue
            tSum[i] += jobs[pos]
            self.dfs(jobs, pos - 1, tSum)
            tSum[i] -= jobs[pos]

"""
古城算法
https://www.youtube.com/watch?v=XUENq5Mxr4I

主要是剪枝把，使用了以下技巧
- 排序，并从大到小分配工作，增加分配的有效性
- 提前结束不可能的case
- 跳过重复的case
"""