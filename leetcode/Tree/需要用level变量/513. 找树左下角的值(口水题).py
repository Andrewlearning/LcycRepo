# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = None
        self.level = -1
        self.helper(root, 0)
        return self.res

    def helper(self, root, level):
        if not root:
            return

        if level > self.level:
            self.level = level
            self.res = root.val

        self.helper(root.left, level + 1)
        self.helper(root.right, level + 1)


