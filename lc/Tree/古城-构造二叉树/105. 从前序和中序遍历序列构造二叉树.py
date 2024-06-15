"""
前序遍历 preorder = [3,9,20,15,7]  root left right
中序遍历 inorder = [9,3,15,20,7]   left root right
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # pre: root,left,right
        # in: left,root,right
        # key:inorder的值 value:值在数组里的下标
        inm = {}
        n = len(preorder)

        # 记录inorder的下标在map里，使得获取下标时时间复杂度为O(1)，这是一个最优化的做法
        for i in range(n):
            inm[inorder[i]] = i
        self.preidx = 0

        def helper(l, r):
            # 当遍历到只有最后一个叶节点时
            # 从inorder来看在当前l~r的区间内，没有val可以使用了，所以可以返回None
            if l > r:
                return None

            # 因为preOrder是 root,left,right
            # 第一个节点总是其他节点的根节点，所以我们preorder的第一个节点作为root构造树
            root = TreeNode(preorder[self.preidx])
            # 每次构造完一个root节点后，都需要把preOrderIndex +1，用于构造下一个root
            self.preidx += 1

            # 获取这个根节点在 inOrder中的下标
            # root下标的左边是左子树，下标的右边是右子树
            idx = inm[val]
            root.left = helper(l, idx - 1)
            root.right = helper(idx + 1, r)

            return root

        return helper(0, n - 1)

"""
古城算法 O(n) 22:00
https://www.bilibili.com/video/BV1jb4y1974B

preOrder: root, left, right
inOrder: left, root, right

每次我们获取preOrder的root节点，作为根节点 [3,9,20,15,7] -> root = 3
然后找到这个root节点在inorder里的下标，下标左边作为root.left, 下标右边作为root.right
[9,(3),15,20,7] -> left=[9] root=3 right=[20,15,7]

可以和106题相互参考
"""