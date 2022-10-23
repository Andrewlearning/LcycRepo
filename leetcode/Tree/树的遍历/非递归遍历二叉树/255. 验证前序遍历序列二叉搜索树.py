"""
给定一个整数数组，你需要验证它是否是一个二叉搜索树正确的先序遍历序列。
你可以假定该序列中的数都是不相同的。
参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3

示例 1：
输入: [5,2,6,1,3]
输出: false
示例 2：
输入: [5,2,1,3,6]
输出: true
"""


class Solution(object):
    # 如果出现递减序列，则是左子树
    # 否则是右子树，右子树一定是递增的
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """

        stack = []
        new_min = float("-inf")

        for node in preorder:
            # 因为node在左子树时，不会更新new_min
            # 当到右子树时，才会更新new_min,当在右子树时，应该是处于一个递增的阶段，所以用这个来判断
            if node < new_min:
                return False

            # root left right
            # 当我们的Node把左子树遍历完了，开始要遍历右子树的时候
            # 那么就会把stack里小与右子树的节点的全部pop掉
            # 假如顺序正确的话，new_min当前node的父节点（因为left root都比right小，但是root最晚出来）
            while stack and node > stack[-1]:
                new_min = stack.pop(-1)

            stack.append(node)

        return True

"""
https://leetcode-cn.com/problems/verify-preorder-sequence-in-binary-search-tree/solution/python3-tu-jie-by-ml-zimingmeng/

如果出现递减序列，则是左子树
否则是右子树，右子树一定是递增的
"""

