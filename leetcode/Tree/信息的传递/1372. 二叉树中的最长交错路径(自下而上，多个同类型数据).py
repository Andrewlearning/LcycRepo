"""
给你一棵以 root 为根的二叉树，二叉树中的交错路径定义如下：

选择二叉树中 任意 节点和一个方向（左或者右）。
如果前进方向为右，那么移动到当前节点的的右子节点，否则移动到它的左子节点。
改变前进方向：左变右或者右变左。
重复第二步和第三步，直到你在树中无法继续移动。
交错路径的长度定义为：访问过的节点数目 - 1（单个节点的路径长度为 0 ）。

请你返回给定树中最长 交错路径 的长度。
"""

class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root)
        # 最长zigzag路径需要排除掉路径的第一个节点
        return self.res - 1

    def dfs(self, root):
        # 记录在当前节点，往下走，所能构成的zigzag节点有多长
        # res[0]代表，当前节点的左节点为开头，所能构成的zigzag长度
        # res[1]代表，当前节点的右节点为开头，所能构成的zigzag长度
        res = [0, 0]
        if not root:
            return res

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        # 无论下面结果如何，在这一层都把自己的节点加进去，因为对于上面节点来说，这一层可以作为上面的左或者右
        # 当前节点与左子树开始所能构成的最长zigzag路径 = 当前节点 + 左节点的右子树所能构成的最长zigzag路劲
        # 当前节点与右子树开始所能构成的最长zigzag路径 = 当前节点 + 右节点的左子树所能构成的最长zigzag路劲
        res[0] = left[1] + 1
        res[1] = right[0] + 1

        # 每轮都重新记录下最长zigzag路径
        self.res = max(self.res, max(res[0], res[1]))
        return res


"""
https://www.youtube.com/watch?v=10-xBLiytBA&t=95s 36：00
"""