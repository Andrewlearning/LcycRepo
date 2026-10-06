"""
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, l: TreeNode | None, r: TreeNode | None) -> bool:
        if l == None and r == None:
            return True
        if l == None or r == None:
            return False
        if l.val != r.val:
            return False
        
        return self.isSameTree(l.left, r.left) and self.isSameTree(l.right, r.right)
    
# 时间复杂度：O(min(N, M))
# 空间复杂度：O(min(H_L, H_R))

# 一句话解析
# 时间：采用 DFS 同步遍历两棵树，只要遇到结构不同或节点值不同就会触发剪枝立即返回，因此最多只需遍历较小那棵树的节点数 min(N, M)。
# 
# 空间：取决于递归栈的最大深度，
# 由于dfs是先遍历完一边再，回退到顶，然后再遍历另一边，所以递归栈的最大深度为两棵树中较矮树的高度，即 O(min(H_L, H_R))，其中 H_L 和 H_R 分别为两棵树的高度。
# 最坏情况（单链树）为 O(min(N, M))，最好情况（平衡树）为 O(log(min(N, M)))。
