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
        if not root:
            return True

        return self.helper(root.left, root.right)

    # 我们把需要判断是否对称的节点，放在left和right
    def helper(self, left, right):
        # 假如说两个节点都为空，那么说明走过的路上面所有的节点都是满足条件的
        if not left and not right:
            return True

        # 假如说一个有一个没，那么肯定堆成不了
        if not left or not right:
            return False

        # 当两个节点的值都不相等的话，那么返回FALSE
        if left.val != right.val:
            return False

        # 判断最外侧的两个节点是否对称 and 判断最里面的两个节点是否对称
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)

# 跟100类似