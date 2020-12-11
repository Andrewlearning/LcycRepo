"""
给定一个二叉树，我们在树的节点上安装摄像头。

节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。

计算监控树的所有节点所需的最小摄像头数量。
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.state = {"None": 0, "cover": 1, "camera": 2}
        self.res = 0

        # 贪心到最上面了，说明下面两个节点是有其中一个节点处于被监控状态
        # 因为没有更好的放相机的选择了，那只好放在root这里
        if self.postOrder(root) == self.state["None"]:
            self.res += 1

        return self.res

    def postOrder(self, root):
        if not root:
            return self.state["cover"]

        # 后续遍历保证是从下往上放监控的（贪心，为啥？）
        left = self.postOrder(root.left)
        right = self.postOrder(root.right)

        # 假如说下面两个顶点，都是未被监控的状态，那么当前节点应该放监控
        if left == self.state["None"] or right == self.state["None"]:
            self.res += 1
            return self.state["camera"]

        # 假如下面两个顶点其中一个有相机，那么当前节点就是被cover
        if left == self.state["camera"] or right == self.state["camera"]:
            return self.state["cover"]

        # 假如下面两个节点并没有相机，然后其中有节点是被监控的，说明不应该再当前点放监控
        # 所以把当前节点设为None
        return self.state["None"]

# https://zxi.mytechroad.com/blog/tree/leetcode-968-binary-tree-cameras/