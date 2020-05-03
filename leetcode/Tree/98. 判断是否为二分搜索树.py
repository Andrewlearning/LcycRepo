"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
判断这棵树是不是二叉搜索树
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#1
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return
        return self.helper(root, -float('inf'), float('inf'))

    def helper(self, root, min, max):
        if not root:
            return True

        if min != None and root.val <= min: return False
        if max != None and root.val >= max: return False
        return self.helper(root.left,min,root.val) and self.helper(root.right,root.val,max)

#2
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        self.prenode = None
        return self.helper(root)

    def helper(self, root):
        if not root:
            return True

        if not self.helper(root.left):
            return False

        #因为是按照左中右的顺序来的，根据BST，我们要保证当前的node的值一定是大于上一个node的
        #如果违反则说明啥是错了
        if self.prenode and root.val <= self.prenode.val:
            return False

        self.prenode = root

        return self.helper(root.right)


"""
答案：
有三种解法：
1。给个把root,他所应当的最大值，和最小值给放进去。假如在左子树，那么左子树的每个点都不可以大于root.val
假如在右子树，那么每个node。都不能小于root.val 。 遍历到node == None 就返回True
2.BST我们就要想到中序遍历法，这个中序遍历法在于，跑一个中序遍历，且记录每上一次循环的node,当前的root.val > pre.val，假如说不符合则返回false.然后其中有很多奇奇怪怪的限制条件，水平不够，最好别写这个，怕错了

"""