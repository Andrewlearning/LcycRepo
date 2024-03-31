# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return self.helper(root)

    def helper(self, root):
        if not root:
            return 0

        # 分别求到左右子树的最大深度
        left = self.helper(root.left)
        right = self.helper(root.right)

        # 返回当前节点的层数 + 当前节点子树的层数
        return 1 + max(left, right)