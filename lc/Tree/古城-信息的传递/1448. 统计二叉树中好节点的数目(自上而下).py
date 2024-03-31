"""
给你一棵根为 root 的二叉树，请你返回二叉树中好节点的数目。

「好节点」X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值。
"""
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root, float('-inf'))
        return self.res

    def dfs(self, root, maxValue):
        if not root:
            return
        if root.val >= maxValue:
            self.res += 1
        self.dfs(root.left, max(root.val, maxValue))
        self.dfs(root.right, max(root.val, maxValue))

"""
https://www.youtube.com/watch?v=10-xBLiytBA&t=95s 16:35
自上而下传递当前path到目前为止的最大值，假如当前节点>=这条path之前的最大值，则记录
"""