"""
给你一个数组，数组里有梯子和蛇
用户每回合可以丢一次色子，范围为1-6，表示用户可以向前走1-6步
当用户前进结束碰到梯子可以快进，碰到蛇会倒退
且每回合用户只能快进一次或倒退一次

求用户从左下角出发，最少需要走几回合可以到达终点右上角

[
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]
]

Output: 4
Explanation:
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.
"""

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        # 终点
        target = n * n

        # 这里可以用heap，也可以用deque，但是感觉用heap比较make sense一点，虽然最后好像差别不大
        # heap: (step, cur position)
        heap = [(0, 1)]

        # 记录走过的点，假如走过，就不用重新走一遍了
        visited = set()

        while heap:
            step, cur = heapq.heappop(heap)

            # 可以摇色子，范围是1-6
            for i in range(1, 7):
                nxt = cur + i
                if nxt > target:
                    continue

                # 判断nxt的位置是不是蛇或者梯子，假如是的话，直接让nxt=蛇或梯子指向的位置
                x, y = self.conv(n, nxt)
                if board[x][y] != -1:
                    nxt = board[x][y]

                # 到达终点
                if nxt == target:
                    return step + 1

                # 没到达终点，则记录，并遍历到下一个节点
                if nxt not in visited:
                    visited.add(nxt)
                    heapq.heappush(heap, (step + 1, nxt))

        return -1

    # 把 数字转换成棋盘的位置
    def conv(self, n, val):
        # 因为在下标是从0开始，但是数字是从1开始，所以要-1来得到下标
        row = (val - 1) // n
        col = (val - 1) % n

        # 奇数行col的值是反过来的
        if row % 2 == 1:
            col = n - 1 - col

        # row的值也是反过来的
        row = n - 1 - row

        return row, col

"""
比acwing好懂
https://github.com/Christinezy/Leetcode/blob/main/Hashmap/149.%20%E7%9B%B4%E7%BA%BF%E4%B8%8A%E6%9C%80%E5%A4%9A%E7%9A%84%E7%82%B9%E6%95%B0.py
"""