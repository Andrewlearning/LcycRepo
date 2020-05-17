# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        if not A or not B:
            return False

        return self.helper(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def helper(self, A, B):
        # 这里是本题和572产生区别的地方
        # 因为本题要求的是树的子结构，意思就是说，不一定需要子树的所有节点都完全匹配
        # 我们要求的是，只要B树有的节点，都要和A树完全对上
        # 而不是要求，只要A树有的节点，B树要完全对上(572)
        # 可以看例子
        if not B:
            return True
        # 当任意一棵树遍历完后， 另外一棵树还存在节点，那么说明出错了
        if not A or not B:
            return False

        return A.val == B.val and self.helper(A.left, B.left) and self.helper(A.right, B.right)

"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1

对于本题来说，这个是对的， 
但是对于527来说，子树要变成，才是对的
   4 
  / \
 1   2
"""