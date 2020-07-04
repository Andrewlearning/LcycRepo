"""
给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。

返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution(object):
    def distanceK(self, root, target, K):
        def dfs(node, par=None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        # 先利用dfs构造一个无向图,使每个节点不但能和left,right相连
        # 还可以跟父节点相连
        dfs(root)

        queue = collections.deque([(target, 0)])
        visited = {target}
        while queue:
            # 当出现距离等于k的节点时
            # 说明距离为k-1的节点已经走完，距离为k+1的节点尚未加进去
            # 所以我们可以把所有queue节点都放进res
            if queue[0][1] == K:
                return [node.val for node, d in queue]

            # 取出节点，和距离
            node, d = queue.popleft()

            # 看node周边节点有哪些没有去过，然后进行bfs遍历
            for nei in (node.left, node.right, node.par):
                if nei and nei not in visited:
                    visited.add(nei)
                    queue.append((nei, d + 1))

        return []
