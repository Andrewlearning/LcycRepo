# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        self.res = []
        self.helper(root, [], target)
        return self.res

    def helper(self, root, path, target):
        # print(root.val, path, target)
        if not root:
            return False

        if not root.left and not root.right and target == root.val:
            self.res.append(path + [root.val])
            return

        if root.left:
            self.helper(root.left, path + [root.val], target - root.val)
        if root.right:
            self.helper(root.right, path + [root.val], target - root.val)






"""
等于lc pathsum 2
"""
