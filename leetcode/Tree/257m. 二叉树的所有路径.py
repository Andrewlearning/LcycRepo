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
            # 每成功遍历一个node,才把这个node给放进去
            string += str(root.val)

            # 假如说路径已经结束，那就把结果给放进去
            if not root.left and not root.right:
                self.res.append(string[:])
            # 假如说路径还没结束，那么加上->, 进入下一个循环
            else:
                string += "->"
                self.helper(root.left, string)
                self.helper(root.right, string)

"""
时间复杂度：O(N^2) 其中 N 表示节点数目。在深度优先搜索中每个节点会被访问一次且只会被访问一次，每一次会对 path 变量进行拷贝构造，时间代价为 O(N)，故时间复杂度为 O(N^2)

空间复杂度：O(N^2)其中 N 表示节点数目。除答案数组外我们需要考虑递归调用的栈空间。
在最坏情况下，当二叉树中每个节点只有一个孩子节点时，即整棵二叉树呈一个链状，此时递归的层数为 NN，此时每一层的 path 变量的空间代价的总和为 O
​	
https://leetcode-cn.com/problems/binary-tree-paths/solution/er-cha-shu-de-suo-you-lu-jing-by-leetcode-solution/
"""
