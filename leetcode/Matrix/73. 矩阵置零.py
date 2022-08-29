"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:
Input:
[[1,1,1],
[1,0,1],
[1,1,1]]
Output:
[[1,0,1],
[0,0,0],
[1,0,1]]
把列表中的0的横轴竖轴都变成0。
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        lrow = len(matrix)
        lcol = len(matrix[0])

        rows = [0] * lrow
        cols = [0] * lcol

        for i in range(lrow):
            for j in range(lcol):
                # 因为某一个位置为0，那么那个位置的行和列都为0，所以把该行和列都标为1
                if matrix[i][j] == 0:
                    rows[i] = cols[j] = 1

        for i in range(lrow):
            for j in range(lcol):
                # 假如碰到被标记的行和列，就把matrix改为0
                if rows[i] == 1 or cols[j] == 1:
                    matrix[i][j] = 0
        return matrix

"""
https://algocasts.io/episodes/nwp8gDG7
Time: O(m*n) space:O(m+n)
答案：
采用了第一种做法，没这么抽象
1.因为当我们找到一个0，就要把该0所在的行和列都变成0
2.所以我们用两个数组 rows,cols来分别表示第几行和第几列，当找到一个数为0，那我们就在相应的行列里左上标记
例如 [1,1]为0，那么row = [0,1,0] col = [0,1,0]
3.之后我们再整体遍历一遍数组，当我们发现row or col在当前位置被标记过，说明这个位置应该是0，那么把它变成0
"""