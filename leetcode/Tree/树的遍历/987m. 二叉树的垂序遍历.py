"""
给定二叉树，按垂序遍历返回其结点值。

对位于(X, Y)的每个结点而言，其左右子结点分别位于(X-1, Y-1)和(X+1, Y-1)。

把一条垂线从X = -infinity 移动到X = +infinity，
每当该垂线与结点接触时，我们按从上到下的顺序报告结点的值（ Y坐标递减）。

如果两个结点位置相同，则首先报告的结点值较小。

按X坐标顺序返回非空报告的列表。每个报告都有一个结点值列表。
"""
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        # key = col(横坐标)
        # val = [row(纵坐标,height), node] in this col
        self.s = defaultdict(list)

        self.dfs(root, 0, 0)

        res = []
        for col in sorted(self.s.keys()):
            # 由于s[col]中是 [row1, v1], [row2, v2]
            # 我们需要先按照row的从小到大输出，且当row相等时，得按值从小到大输出，这样sort刚好满足条件
            res.append(p[1] for p in sorted(self.s[col]))
        return res

    # 前序遍历所有节点
    def dfs(self, root, height, col):
        if not root:
            return
        self.s[col].append([height, root.val])
        self.dfs(root.left, height + 1, col - 1)
        self.dfs(root.right, height + 1, col + 1)

"""
本题与314一样
https://www.acwing.com/video/3295/
"""