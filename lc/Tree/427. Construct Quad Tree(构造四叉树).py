"""
Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.

Return the root of the Quad-Tree representing grid.

A Quad-Tree is a tree data structure in which each internal node has exactly four children.
Besides, each node has two attributes:

val: True if the node represents a grid of 1's or False if the node represents a grid of 0's.
Notice that you can assign the val to True or False when isLeaf is False, and both are accepted in the answer.

isLeaf: True if the node is a leaf node on the tree or False if the node has four children.
"""

"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        n = len(grid)
        return self.bfs(grid, 0, 0, n)

    # i,j 表示最左上角的正方形的坐标
    def bfs(self, grid, i, j, length):
        # base case, 最小单位，就是只有一个方块了，这个方块肯定是一个叶子节点，并且不可能构成四叉树
        if length == 1:
            return Node(grid[i][j], True, None, None, None, None)

        half = length // 2
        # 构建四个子树，分别代表四个方向的
        topLeft = self.bfs(grid, i, j, half)
        topRight = self.bfs(grid, i, j + half, half)
        bottomLeft = self.bfs(grid, i + half, j, half)
        bottomRight = self.bfs(grid, i + half, j + half, half)

        # 首先检查子网格是否是叶子节点，如果是，它创建一个只有一个节点的子树 并将isLeaf属性设置为True
        if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and \
                (topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
            return Node(topLeft.val, True, None, None, None, None)
        else:
            # 如果这四个子树不全都是叶子节点 ， 将四个子树连接到该节点的属性中
            return Node(grid[i][j], False, topLeft, topRight, bottomLeft, bottomRight)

"""
可以看看y总视频理解题意把，不过解法不是用他的，这种更好懂一点
https://www.acwing.com/activity/content/problem/content/2822/
"""