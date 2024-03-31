class Solution(object):
    def largestIsland(self, grid):
        N = len(grid)
        
        # 只要没有越界，都算neighbors
        def neighbors(r, c):
            res = []
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < N and 0 <= nc < N:
                    res.append([nr, nc])
            return res
        
        # 该联通分量有多少个元素
        def dfs(r, c, color):
            res = 1
            grid[r][c] = color
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    res += dfs(nr, nc, color)
            return res
        
        # 颜色：对应颜色所对应的面积
        area = {}
        color = 2
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    area[color] = dfs(r, c, color)
                    color += 1

        res = max(area.values() or [0])
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    # seen代表着当前0四周有颜色的联通分量的块
                    seen = {grid[nr][nc] for nr, nc in neighbors(r, c) if grid[nr][nc] > 1}
                    # 更新，1代表假如把当前0当做是陆地的话
                    res = max(res, 1 + sum(area[i] for i in seen))
        return res
"""
Time complexity: O(n*m)
Space complexity: O(n*m)
"""
# https://zxi.mytechroad.com/blog/graph/leetcode-827-making-a-large-island/
# 链接：https://leetcode-cn.com/problems/making-a-large-island/solution/zui-da-ren-gong-dao-by-leetcode/
