class Solution:
    def solve(self, board: list[list[str]]) -> None:
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        
        def dfs(r: int, c: int):
            # 超出边界或者不是 'O' 则停止扩散
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'O':
                return
            
            # 标记为 'E' (Escaped)
            board[r][c] = 'E'
            
            # 向上下左右四个方向继续扩散
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. 扫描左右边界列
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
            
        # 2. 扫描上下边界行
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        # 3. 统一重置/翻转
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'  # 被完全包围的 'O' 替换成 'X'
                elif board[r][c] == 'E':
                    board[r][c] = 'O'  # 连通边界的 'O' 还原


"""
解题思路（三步走）
边界扩散（DFS / BFS）：
遍历矩阵的四周边界（第一行、最后一行、第一列、最后一列），凡是遇到 'O'，就从它出发做 DFS
把所有与它直接或间接相连的 'O' 临时标记为 'E'（代表 Escaped / Edge-connected）。

遍历全局替换：
再次遍历整个矩阵：
剩下的 'O'：说明无法到达边界，必定被包围，修改为 'X'。
标记为 'E' 的单元格：说明连通边界，无法被包围，恢复为 'O'。


复杂度分析
时间复杂度：O(M * N)，其中 M 和 N 分别为矩阵的行数和列数。每个格子最多被访问和修改常数次。
空间复杂度：O(M * N)，主要为递归调用的系统栈消耗（最坏情况下整个矩阵都是 'O'）。

"""