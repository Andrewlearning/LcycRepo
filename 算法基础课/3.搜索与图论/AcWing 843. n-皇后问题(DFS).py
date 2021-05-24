def dfs(i):
    # 说明所有的行都放完了，诞生了一个答案
    if i == n:
        for r in range(n):
            for c in range(n):
                print(pt[board[r][c]], end="")
            print()
        print()
        return

    for j in range(n):
        # i = y, j = x
        # 一条从/斜线是(dig)用 y = x + b 表示, b = y - x, 又因为我们只要在b > 0的结果，所以要添加偏移量n
        # 所以从/上(dig)的斜线用 b = y - x + n 表示，其中y是不变的，x是变化的
        # 同理，\ (udig)用 y = -x + b表示，b = y + x，n衡大于0，所以不用添加偏移量
        # 所以从\ (udig)用 b = y + x表示，其中y是不变的，x是变化的

        # 假如说，当前(i,j) 在当前坐标的列，经过改点的/ \上都没有皇后的话，说明当前位置可以放置一个皇后
        if col[j] != 1 and dig[i - j + n] != 1 and udig[i + j] != 1:
            board[i][j] = col[j] = dig[i - j + n] = udig[i + j] = 1
            # 去下一行
            dfs(i + 1)
            board[i][j] = col[j] = dig[i - j + n] = udig[i + j] = 0


if __name__ == "__main__":
    n = int(input())

    # 代表棋盘的列，每一个列都只能放一个元素
    # 因为行的话，我们每次都在一行里操作，所以不会产生重复
    col = [0] * n

    # dig是代表/ 这样的斜线上有没有过元素
    dig = [0] * (2 * n)
    # udig是代表 \ 这样的斜线上有没有过元素
    udig = [0] * (2 * n)

    board = [[0] * n for _ in range(n)]
    pt = {0: '.', 1: 'Q'}
    # 遍历的顺序是，每次只在一行放一个，放完一行再放下一行
    dfs(0)

# idea:https://www.acwing.com/video/275/
# dig 和 udig的转化https://www.acwing.com/solution/content/6245/