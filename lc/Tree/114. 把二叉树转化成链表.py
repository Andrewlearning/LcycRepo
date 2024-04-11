# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
	def __init__(self):
		# 记录前一个节点
		self.pre = None

	def flatten(self, root):
		"""
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

		"""
			我们希望构造成链表的顺序是pre order: root left right
			所以构造的时候要从相反顺序进行构造: right left root
			假如试图从pre order的顺序构造，会发现没办法获得下一个节点，所以不行
		"""
		if not root:
			return

		self.flatten(root.right)
		self.flatten(root.left)

		root.right = self.pre
		root.left = None
		# 当当前node构造完成后，记录在self.pre里面，以供上一层节点进行连接
		self.pre = root

		return root





"""
时间 O(n),遍历n个点，循环n个node
空间 O(n)，建了一个长度为n的list

这题其实不难
1.就是先用前序遍历把所有的节点都加进一个list
2.然后遍历这个list,从root出发，因为这个list都是前序遍历来的
	所以我们把每个拿出来的node.right = 设为下一个点就好了
"""