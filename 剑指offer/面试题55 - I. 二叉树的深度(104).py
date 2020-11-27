# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return self.helper(root, 0)

    def helper(self, root, num):
        if not root:
            return num

        # num + 1表示当前这一层的高度， 因为我们把初始高度设置成了 1
        return max(self.helper(root.left, num + 1), self.helper(root.right, num + 1))



"""
时间复杂度 O(N) ： N 为树的节点数量，计算树的深度需要遍历所有节点。
空间复杂度 O(N) ： 最差情况下（当树退化为链表时），递归深度可达到 N 

链接：https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/solution/mian-shi-ti-55-i-er-cha-shu-de-shen-du-xian-xu-bia/

"""
class Solution:
    def TreeDeep(self, pRoot):
        if not pRoot:
            return 0
        left = self.TreeDeep(pRoot.left)
        right = self.TreeDeep(pRoot.right)
        return left + 1 if left > right else right + 1


