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
做法上是105的相反，因为postorder的root节点是从右向左

时间复杂度： O(n),n 是树的节点数。
    构建哈希表是 O(n)。
    递归遍历树是 O(n),每个节点访问一次。
空间复杂度： O(n),n 是树的节点数。
    哈希表占用 O(n) 空间。
    递归调用栈占用 O(n) 空间，因为最差情况是单链状

"""