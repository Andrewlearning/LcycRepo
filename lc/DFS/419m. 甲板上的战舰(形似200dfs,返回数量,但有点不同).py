"""
给定一个二维的甲板， 请计算其中有多少艘战舰。 战舰用 'X'表示，空位用 '.'表示。 你需要遵守以下规则：

给你一个有效的甲板，仅由战舰或者空位组成。
战舰只能水平或者垂直放置。换句话说,战舰只能由 1xN (1 行, N 列)组成，或者 Nx1 (N 行, 1 列)组成，其中N可以是任意大小。
两艘战舰之间至少有一个水平或垂直的空位分隔 - 即没有相邻的战舰。
示例 :

X..X
...X
...X
在上面的甲板中有2艘战舰。

无效样例 :

...X
XXXX
...X
你不会收到这样的无效甲板 - 因为战舰之间至少会有一个空位将它们分开

"""


class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        res = 0

        # 用一个取巧的方法，只统计最左上方的砖的个数就可
        for i in range(len(board)):
            for j in range(len(board[0])):
                #  假如说上面的那块砖是X，说明当前砖不是最左上方的
                if i > 0 and board[i - 1][j] == "X":
                    continue
                # 假如说左面的那块砖是X，说明当前砖不是最左上方的
                if j > 0 and board[i][j - 1] == "X":
                    continue
                # 假如当前砖是最左上方的，说明这是一艘战舰
                if board[i][j] == "X":
                    res += 1

        return res

"""
https://www.acwing.com/video/1812/
本题其实和200题是一样的，但是唯一不同的地方是，在200题，是允许全图连接的岛屿存在
但是这里由于这种取巧的做法，当有全图连接的夹板时，会被判成无效甲板，不会出现这种案例，要不然这题就
不能用这种方法去解了
"""