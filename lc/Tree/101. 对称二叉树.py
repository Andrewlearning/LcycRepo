# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(l, r):
            if not l and not r:
                return True
            
            if not l or not r:
                return False
            
            if l.val != r.val:
                return False
            
            return helper(l.left, r.right) and helper(l.right, r.left)
        
        return helper(root.left, root.right)

# 跟100类似