"""
n皇后问题是将n个皇后放置在n*n的棋盘上，皇后彼此之间不能相互攻击(任意两个皇后不能位于同一行，同一列，同一斜线)。
题目问给定一个n，能生成几种不同的答案
"""
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0
        # 递归树是发散式的，例如题目给的例子，row=0的时候 col=1 或 3都可以放皇后，这会导致产生两个不同的答案
        self.bt(n, 0, [])
        return self.count

    def bt(self, n, row, queens):
        # 当row移动到最后，都没有冲突时，说明找到一个组合可以在棋盘上摆满皇后，记录答案
        if row == n:
            self.count += 1
            return

        # 每次进入一个backtracking, 我们都给定一个row，然后从0开始遍历col, 看看能不能找到一个合适的(row,col)来放置一个皇后
        for col in range(n):
            if self.safe(row, col, queens):
                # 假如当前row,col可以放皇后，则记录，并且row移动到下一行
                self.bt(n, row + 1, queens + [(row, col)])
        return

    def safe(self, row, col, queens):
        # 看当前位置可不可以放皇后
        for qrow, qcol in queens:
            # 当前row, 和col上不能存在其他皇后
            # abs(qrow - row) == abs(qcol - col) 当前位置的斜线上不能存在其他皇后, 例如[0,2] 和 [1,3] 这两个就是在同一斜线上
            if qrow == row or qcol == col or abs(qrow - row) == abs(qcol - col):
                return False

        return True

"""
答案来自宋姐
Time O(n!), n为n皇后的数量
因为bracktracking在每一行都要尝试n个位置，但由于在每一行都会放置一个皇后，那么往下一行col可以选择的位置都在减少-1
由于只有在往下递归时间复杂度才高，safe()遍历到不可以选择位置的复杂度大约为O(1~n), 时间复杂为 n * n-1 * n-2 .. * 1 = n!

空间复杂度，由于最多row递归n层，所以空间复杂度为 O(n)
"""