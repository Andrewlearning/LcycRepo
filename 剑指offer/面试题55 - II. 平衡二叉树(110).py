"""
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。


示例 1:
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        # 假如返回的高度不是-1， 即表示二叉树是平衡的
        return self.helper(root) != -1


    def helper(self, root):
        # 明确我们的返回是为高度， 所以遍历到最下面一层的时候，返回的是高度0
        if not root:
            return 0

        # 获取左子树的最大高度
        left = self.helper(root.left)
        if left == -1:
            return -1

        # 获取右子树的最大高度
        right = self.helper(root.right)
        if right == -1:
            return -1

        # 看两个子树的最大高度差是不是 > 1
        if abs(left - right) > 1:
            return -1

        # 关键点在这里， 当前高度 = 1 + 下一层的高度
        return 1 + max(left, right)


"""
平衡二叉树（Balanced Binary Tree）它是一棵空树或它的左右两个子树的高度差的绝对值不超过1,意味着其中一边可以是缺一个node的。
这题的做法是要计算每个node的高度差

我的想法：怎么计算高度差。没想法

答案：从上往下，看每个顶点的左右高度差，用二叉树的深度的答案来求
https://blog.csdn.net/u010005281/article/details/79718391
"""