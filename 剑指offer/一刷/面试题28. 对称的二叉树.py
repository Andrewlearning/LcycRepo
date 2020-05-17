"""
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3


"""
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

    def helper(self, left, right):
        # 假如说两个节点都为空，那么说明走过的路上面所有的节点都是满足条件的
        if not left and not right:
            return True

        # 假如说一个有一个没，那么肯定堆成不了
        if not left or not right:
            return False

        # 在确保 当前的对称性满足之后， 我们继续判断下面的节点
        return left.val == right.val and self.helper(left.left, right.right) and self.helper(left.right, right.left)


"""
想到的一种做法就是
把树的每一层都遍历下来，然后在从最左和最右开始向中间遍历


答案：
这种做法是不对的，按照剑指offer的说法
树的正规遍历方法一般是有三种遍历方法，例如前序遍历法 为 前root后
我们可以创造一种镜像前序遍历法， 为后root前
同时一路上保留空节点，把他们都储存在一个list里来比较

然后还有一种做法就是直接用递归来判断；
左树 == 右树， 左树左 == 右树右， 右树左==左树右
做个递归
"""