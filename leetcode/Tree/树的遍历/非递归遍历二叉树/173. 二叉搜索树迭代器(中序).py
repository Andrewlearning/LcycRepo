# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.pushStack(root)

    def pushStack(self, node):
        # 等于把一路向左的节点都丢进stack里面去
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        cur = self.stack.pop(-1)
        # 我们记得用完每一个节点，都要把那个节点的右节点丢进去跑
        if cur.right:
            self.pushStack(cur.right)
        return cur.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

"""
本题等于是把二叉搜索树的中序遍历给拆分了
https://leetcode-cn.com/problems/binary-search-tree-iterator/solution/yong-zhan-mo-ni-zhong-xu-bian-li-guo-cheng-by-powc/
"""