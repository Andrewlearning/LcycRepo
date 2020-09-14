"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。
说明: 叶子节点是指没有子节点的节点。
输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]
解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
"""
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        self.res = []
        self.helper(root, "")
        return self.res

    # 注意思考这里的递归是怎么写的
    def helper(self, root, string):
        if root:
            string += str(root.val)
            if not root.left and not root.right:
                self.res.append(string[:])
            else:
                string += "->"
                self.helper(root.left, string)
                self.helper(root.right, string)

# https://leetcode-cn.com/problems/binary-tree-paths/solution/er-cha-shu-de-suo-you-lu-jing-by-leetcode-solution/