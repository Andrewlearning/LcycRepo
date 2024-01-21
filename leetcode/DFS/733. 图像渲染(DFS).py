"""
有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。

给你一个坐标(sr, sc)表示图像渲染开始的像素值（行 ，列）和一个新的颜色值newColor，让你重新上色这幅图像。

image = [[1,1,1],
        [1,1,0],
        [1,0,1]]

sr = 1, sc = 1, newColor = 2
输出: [[2,2,2],
      [2,2,0],
      [2,0,1]]
解析:
在图像的正中间，(坐标(sr,sc)=(1,1)),
在路径上(上下左右)所有符合条件的像素点的颜色都被更改成2。
注意，右下角的像素没有更改为2，
因为它不是在上下左右四个方向上与初始点相连的像素点。
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
        self.image = image
        self.color = image[sr][sc]
        self.newColor = color
        self.helper(sr, sc)

        return self.image

    def helper(self, sr, sc):
        # self.image[sr][sc] == self.newColor 过滤掉已经处理过的节点，避免死循环
        if not (0 <= sr < len(self.image)) or not (0 <= sc < len(self.image[0])) or self.image[sr][sc] == self.newColor:
            return

        # 假如当前节点颜色，是起始节点的颜色，那么我们才更新
        if self.image[sr][sc] == self.color:
            self.image[sr][sc] = self.newColor
            self.helper(sr + 1, sc)
            self.helper(sr - 1, sc)
            self.helper(sr, sc + 1)
            self.helper(sr, sc - 1)

"""
时间复杂度：O(N)。N 是图片像素的个数。我们可能渲染每一个像素。
空间复杂度：O(N)，调用 dfs 时隐式调用堆栈的大小。
"""