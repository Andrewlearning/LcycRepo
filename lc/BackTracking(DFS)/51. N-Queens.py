"""
n皇后问题是将n个皇后放置在n*n的棋盘上，皇后彼此之间不能相互攻击(任意两个皇后不能位于同一行，同一列，同一斜线)。
题目问给定一个n，能生成几种不同的答案，并记录这些答案

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."], ["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
"""
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = []
        self.temp = []
        self.bt(n, 0, [])
        return self.res

    def bt(self, n, row, queens):
        # 当row移动到最后，都没有冲突时，说明找到一个组合可以在棋盘上摆满皇后，记录答案
        if row == n:
            self.res.append(self.temp[:])
            return

        for col in range(n):
            if self.safe(row, col, queens):
                self.temp.append(self.genLvRes(n, col))
                self.bt(n, row + 1, queens + [(row, col)])
                # 假如你用过了(row,col)这个答案，那么需要把它pop掉，给下一个col来生成本层其他答案
                self.temp.pop()
        return

    def genLvRes(self, n, col):
        res = ""
        for i in range(n):
            if i == col:
                res += "Q"
            else:
                res += "."
        return res

    def safe(self, row, col, queens):
        # 看当前位置可不可以放皇后
        for qrow, qcol in queens:
            # 当前row, 和col上不能存在其他皇后
            # abs(qrow - row) == abs(qcol - col) 当前位置的斜线上不能存在其他皇后, 例如[0,2] 和 [1,3] 这两个就是在同一斜线上
            if qrow == row or qcol == col or abs(qrow - row) == abs(qcol - col):
                return False

        return True

"""
参考52的答案

Time O(n!), n为n皇后的数量
因为bracktracking在每一行都要尝试n个位置，但由于在每一行都会放置一个皇后，那么往下一行col可以选择的位置都在减少-1
由于只有在往下递归时间复杂度才高，safe()遍历到不可以选择位置的复杂度大约为O(1~n), 时间复杂为 n * n-1 * n-2 .. * 1 = n!

空间复杂度，由于最多row递归n层，所以空间复杂度为 O(n)
"""