"""
有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。

给你一个坐标 (sr, sc) 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。

image = [[1,1,1],
        [1,1,0],
        [1,0,1]]

sr = 1, sc = 1, newColor = 2
输出: [[2,2,2],
      [2,2,0],
      [2,0,1]]
解析:
在图像的正中间，(坐标(sr,sc)=(1,1)),
在路径上所有符合条件的像素点的颜色都被更改成2。
注意，右下角的像素没有更改为2，
因为它不是在上下左右四个方向上与初始点相连的像素点。


链接：https://leetcode-cn.com/problems/flood-fill

"""
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.lr = len(image)
        self.lc = len(image[0])
        self.visited = [[0 for j in range(self.lc)] for i in range(self.lr)]

        for r in range(self.lr):
            for c in range(self.lc):
                if r == sr and c == sc:
                    self.dfs(image, image[sr][sc], newColor, r, c)

        return image

    def dfs(self, image, curcolor, newcolor, r, c):
        if r < 0 or c < 0 or r >= self.lr or c >= self.lc or self.visited[r][c] == 1:
            return

        image[r][c] = newcolor
        self.visited[r][c] = 1

        for dir in self.dirs:
            new_r = r + dir[0]
            new_c = c + dir[1]
            if 0 <= new_r < self.lr and 0 <= new_c < self.lc and image[new_r][new_c] == curcolor:
                self.dfs(image, curcolor, newcolor, new_r, new_c)

        self.visited[r][c] == 0

"""
时间复杂度：O(N)。N 是图片像素的个数。我们可能渲染每一个像素。
空间复杂度：O(N)，调用 dfs 时隐式调用堆栈的大小。

这题跟别的题不一样的地方是：

1. 题目给了你一个扩散的点，从那个点开始做dfs就好了
2. 给定的值并不唯一， 所以我们要传一个原始值进去， 然后再传一个改变值进去， 发现与原始值一样的块我们才去改变
"""