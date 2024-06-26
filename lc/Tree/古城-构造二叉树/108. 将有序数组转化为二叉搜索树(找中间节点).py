"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return

        return self.helper(0, len(nums) - 1, nums)

    def helper(self, start, end, nums):
        if start > end:
            return

        mid = (start + end) // 2
        root = TreeNode(nums[mid])

        root.left = self.helper(start, mid - 1, nums)
        root.right = self.helper(mid + 1, end, nums)

        return root


"""
时间复杂度：每个元素只访问一次。o(N)
空间复杂度：二叉搜索树空间 O(N)，递归栈深度 O(logN)。

https://algocasts.io/episodes/rLmP98Go
我们似乎不用太过在意这个mid 到底是在正中间，还是在正中间偏左， 正中间偏右
因为是二叉搜索树，偏左还是偏右体现的差别应该是左子树多一个节点 还是右子树多一个节点，
不影响构造高度差的绝对值不超过 1的树

"""