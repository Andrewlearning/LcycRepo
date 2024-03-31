"""
你这个学期必须选修 num 门课程，记为0到num - 1 。

在选修某些课程之前需要一些先修课程。
先修课程按数组prereq 给出，其中prereq[i] = [ai, bi] ，
表示如果要学习课程ai 则 必须 先学习课程 bi 。

例如，先修课程对[0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false

输入: 2, [[1,0],[0,1]]
输出: false
解释:总共有 2 门课程。学习课程 1 之前，你需要先完成课程 0
并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
"""
class Solution(object):
    def canFinish(self, num, prereq):
        """
        :type num: int
        :type prereq: List[List[int]]
        :rtype: bool
        """
        if not prereq and len(prereq) == 0:
            return True

        from collections import defaultdict
        # 初始化图, 节点为 pre -> [next1, next2], 先修课 指向 后修课
        graph = defaultdict(list)
        # 初始化入度，pre -> next -> 0
        # pre 的入度为0，因为每节点指向pre
        # next 入度为1，因为pre指向它
        indegree = defaultdict(int)

        for next, pre in prereq:
            # 开始给图的顶点赋予意义，先修课->[下一节课]
            graph[pre].append(next)

            # 构造入度表 node:指向这个node的节点数量有多少
            indegree[next] += 1


        # 把入度为0的点都加入到queue里去
        queue = []
        for node in range(num):
            if indegree[node] == 0:
                queue.append(node)

        # count记录我们总共已经上过了几门课，假如有课不可到达，那么count是不可能 == numCourse的
        # 等于numcourse的
        count = 0
        while queue:
            count += 1
            pre = queue.pop(0)

            # 删除上一个节点pre，所以与之对应pre节点的下一层节点所有的入度都要-1
            for next in graph[pre]:
                indegree[next] -= 1

                # 把入度为0的下一层节点加入到queue
                if indegree[next] == 0:
                    queue.append(next)

        return count == num

"""
time(V+E) Space(V+E)
1. 建立图
2. 建立入度
3. 找入口, 本题是从入度为0的开始
4. BFS 拓扑排序
"""