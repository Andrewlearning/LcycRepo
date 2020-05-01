"""
你被给定一个 m × n 的二维网格，网格中有以下三种可能的初始化值：

-1 表示墙或是障碍物
0 表示一扇门
INF 无限表示一个空的房间。然后，我们用 2147483647 代表 INF。你可以认为通往门的距离总是小于 2147483647 的。
你要给每个空房间位上填上该房间到 最近 门的距离，如果无法到达门，则填 INF 即可。

示例：
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
运行完你的函数后，该网格应该变成：
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        inf = 2147483647
        lrow = len(rooms)
        if lrow == 0:
            return

        lcol = len(rooms[0])
        queue = []

        for r in range(lrow):
            for c in range(lcol):
                # 我们从每个门开始进行宽度优先遍历
                if rooms[r][c] == 0:
                    queue.append([r, c])

        while queue:
            point = queue.pop(0)
            # 因为我们要用这个原本坐标 去和四个方向的坐标相加，所以这里要单独取出来
            row = point[0]
            col = point[1]

            for dir in dirs:

                r = row + dir[0]
                c = col + dir[1]
                # 当坐标越界， 或者说坐标不在 inf上的时候，说明这个点不能走
                if r < 0 or c < 0 or r >= lrow or c >= lcol or rooms[r][c] != inf:
                    continue

                rooms[r][c] = rooms[row][col] + 1
                queue.append([r, c])

"""
Time: O(nm) 我们首先考虑只有一个门的情况，宽度优先搜索最多只需要 m×n 步就能到达所有的房间
Space: O(nm) 空间复杂度与队列的大小有关。我们最多将 m×n 个位置插入队列，所以空间最大为 m×n
https://leetcode-cn.com/problems/walls-and-gates/solution/qiang-yu-men-by-leetcode/


"""

