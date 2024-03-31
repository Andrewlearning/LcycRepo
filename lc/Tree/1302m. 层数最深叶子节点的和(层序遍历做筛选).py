"""
给你一棵二叉树，请你返回层数最深的叶子节点的和。
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        queue = [[root, 0]]
        maxDeep = -1
        total = 0

        while queue:
            cur, depth = queue.pop(0)

            # 更新最大深度
            if depth > maxDeep:
                maxDeep = depth
                total = cur.val
            # 当发现最大深度相等时，total += cur.val
            elif depth == maxDeep:
                total += cur.val

            if cur.left:
                queue.append([cur.left, depth + 1])
            if cur.right:
                queue.append([cur.right, depth + 1])

        return total

# https://leetcode-cn.com/problems/deepest-leaves-sum/solution/ceng-shu-zui-shen-xie-zi-jie-dian-de-he-by-leetc-2/