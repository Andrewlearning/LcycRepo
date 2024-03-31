# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.helper(root)
        # 选择抢当前 和不抢当前最大的更大的那一个
        return max(res[0], res[1])

    def helper(self, root):
        if not root:
            return [0, 0]

        # cur[0]表示偷当前节点的值，cur[1]表示不偷当前节点的值
        cur = [0, 0]
        left = self.helper(root.left)
        right = self.helper(root.right)

        # 假如说，不偷当前节点的值，那么左节点和右节点，我们都可以选择偷他们或者不偷
        # 就是一种很随心所欲的状态，我们可以选择偷或者不偷
        cur[0] = max(left[0], left[1]) + max(right[0], right[1])

        # 假如说，偷当前节点的值，那么左节点和右节点，我们都不能偷
        cur[1] = root.val + left[0] + right[0]

        return cur

"""
https://www.youtube.com/watch?v=-i2BFAU25Zk
这题是树状递归
每个节点我们都创造一个数组，temp,
temp[0]代表不抢劫当前node的最大值
temp[1]代表，抢劫当前node的最大值
我们通过left,right递归完后面的所有节点，来往上推，就能得到temp两种选择的最值
最后我们返回两种选择中的较大值即可
"""

