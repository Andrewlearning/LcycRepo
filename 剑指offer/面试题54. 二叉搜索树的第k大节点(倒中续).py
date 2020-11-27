# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # 因为中序遍历 产生的顺序是递增顺序
    # 而我们要向求第k大的节点的话， 那么就要 从右向左遍历
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return -1

        self.k = k
        self.res = 0
        self.helper(root)

        return self.res

    # reverse -> right root left
    def helper(self, root):
        if not root or self.k < 0:
            return

        self.helper(root.right)

        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return

        self.helper(root.left)

"""
Time: O(n)
Space: O(n)
https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/solution/mian-shi-ti-54-er-cha-sou-suo-shu-de-di-k-da-jie-d/
"""