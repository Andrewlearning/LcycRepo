"""
你被安排了 n个任务。任务需要花费的时间用长度为 n的整数数组tasks表示，第 i个任务需要花费tasks[i]小时完成。
一个 工作时间段中，你可以 至多连续工作sessionTime个小时，然后休息一会儿。

你需要按照如下条件完成给定任务：

如果你在某一个时间段开始一个任务，你需要在 同一个时间段完成它。
完成一个任务后，你可以 立马开始一个新的任务。
你可以按 任意顺序完成任务。
给你tasks 和sessionTime，请你按照上述要求，返回完成所有任务所需要的最少数目的工作时间段。

测试数据保证sessionTime 大于等于tasks[i]中的最大值。

示例 1：

输入：tasks = [1,2,3], sessionTime = 3
输出：2
解释：你可以在两个工作时间段内完成所有任务。
- 第一个工作时间段：完成第一和第二个任务，花费 1 + 2 = 3 小时。
- 第二个工作时间段：完成第三个任务，花费 3 小时。
"""

class Solution(object):
    def minSessions(self, tasks, sessionTime):
        """
        :type tasks: List[int]
        :type sessionTime: int
        :rtype: int
        """
        # 把工作从小到大排序
        tasks.sort()

        # 最差结果是每一个job都需要一个session来做
        self.res = len(tasks)

        # 记录每个session所分配的任务量
        self.sessions = [0] * len(tasks)
        self.tasks = tasks
        self.maxSessionTime = sessionTime
        self.dfs(len(tasks) - 1, 0)
        return self.res

    # sessioncnt 我们需要多少个session
    def dfs(self, taskid, sessioncnt):
        # 需要的session数量，已经大于之前最优解了，剪枝
        if sessioncnt > self.res:
            return

        # 说明已经遍历完所有的task了，需要取一个最终结果
        if taskid < 0:
            self.res = min(self.res, sessioncnt)
            return

        # 遍历self.session[0~sessioncnt], 因为之前的session可能没有完全分配完任务
        for i in range(sessioncnt):
            # 看看能不能往老的session里加工作
            if self.sessions[i] + self.tasks[taskid] <= self.maxSessionTime:
                self.sessions[i] += self.tasks[taskid]
                self.dfs(taskid - 1, sessioncnt)
                self.sessions[i] -= self.tasks[taskid]

        # 老的加不了了，看看能不能往新的session里加工作
        self.sessions[sessioncnt] += self.tasks[taskid]
        self.dfs(taskid - 1, sessioncnt + 1)
        self.sessions[sessioncnt] -= self.tasks[taskid]


"""
古城算法
https://www.youtube.com/watch?v=XUENq5Mxr4I

主要是剪枝把，使用了以下技巧
- 排序，并从大到小分配工作，增加分配的有效性
- 提前结束不可能的case
"""