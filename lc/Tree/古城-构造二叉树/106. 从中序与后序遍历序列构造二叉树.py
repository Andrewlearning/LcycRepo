# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        self.p = postorder
        self.pi = n - 1

        self.im = {}
        for i in range(n):
            self.im[inorder[i]] = i

        return self.h(0, n - 1)

    def h(self, l, r):
        if l > r:
            return None

        node = TreeNode(self.p[self.pi])
        self.pi -= 1

        # 注意这里的遍历的顺序，postorder是 left, right, root
        # 所以这里也要按照这个顺序构建
        nindex = self.im[node.val]
        node.right = self.h(nindex + 1, r)
        node.left = self.h(l, nindex - 1)

        return node

"""
对于这种题， 我们首先先要把root节点找出来， 然后进行左右分堆递归
因为 postorder是 left, right, root, 所以把root抽出来后， 下一个节点是right的
所以我们要把先遍历右子树
然后才遍历左子树
可以与105题相互参考
"""