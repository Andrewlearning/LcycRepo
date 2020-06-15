"""
给定一个 N 叉树，找到其最大深度。
最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
例如，给定一个 3叉树

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0

        return self.helper(root)

    def helper(self, root):
        if not root:
            return 0

        # 找出所有孩子节点中深度最大的
        max_child = 0
        for child in root.children:
            max_child = max(max_child, self.helper(child))


        # 返回当前节点的层数 + 当前孩子树中的最大的层数
        return 1 + max_child

"""
复用104的方法
"""