"""
每个列表里面，代表i下一步能去的节点
那些不会构成死循环的点，就是安全的点

示例：
输入：graph = [[1,2],[2,3],[5],[0],[5],[],[]]
输出：[2,4,5,6]
这里是上图的示意图。
"""


class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        N = len(graph)
        safe = [False] * N

        # 记录cur-> next 有哪些节点，去不了下一个节点的点，是安全的点
        outOrder = graph
        # 记录 next-> cur 有哪些节点
        inOrder = [[] for _ in range(N)]
        queue = []

        # 把出度为0的点，放到queue里去
        for curNode, nextNodes in enumerate(outOrder):
            if not nextNodes:
                queue.append(curNode)

            # 否则则更新出度的list
            for nextNode in nextNodes:
                inOrder[nextNode].append(curNode)

        while queue:
            # 那出度为0的节点pop出来，因为出度为0代表着不会构成死循环，所以是安全的
            curNode = queue.pop(0)
            # 记录这个安全的点
            safe[curNode] = True

            # 删除curNode后，更新所有出度点
            for nextNode in inOrder[curNode]:

                outOrder[nextNode].remove(curNode)
                if len(outOrder[nextNode]) == 0:
                    queue.append(nextNode)

        # 我们要按顺序搞出结果
        return [i for i in range(len(safe)) if safe[i]]