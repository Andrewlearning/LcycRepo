# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
	def flatten(self, root):
		"""
		:type root: TreeNode
		:rtype: None Do not return anything, modify root in-place instead.
		"""
		if not root:
			return []

		stack = [root]
		pre = None

		while stack:
			cur = stack.pop(-1)

			if pre:
				pre.right = cur
				pre.left = None

			if cur.right:
				stack.append(cur.right)

			if cur.left:
				stack.append(cur.left)

			pre = cur

	  # 方法3：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by--26/





"""
时间 O(n),遍历n个点，循环n个node , 空间  O(n)，建了一个长度为n的list
这题其实不难
1.就是先用前序遍历把所有的节点都加进一个list
2.然后遍历这个list,从root出发，因为这个list都是前序遍历来的
	所以我们把每个拿出来的node.right = 设为下一个点就好了
"""