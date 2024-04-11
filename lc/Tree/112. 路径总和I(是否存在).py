"""
判断从最上面的根节点到最下面的叶节点，是否存在一条路，使得他们的和等于sum

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.helper(root, sum)

    def helper(self, root, ts):
        if not root:
            return False

        ts -= root.val
        # 必须是要到根节点的时候没有 sum=target才满足条件
        if ts == 0 and not root.left and not root.right:
            return True

        return self.helper(root.left, ts) or self.helper(root.right, ts)

"""
答案：
还是切树三件套，helper, if not root, 以及终止条件
"""