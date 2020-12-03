"""
给定圆的半径和圆心的 x、y 坐标，写一个在圆中产生均匀随机点的函数 randPoint 。

说明:

输入值和输出值都将是浮点数。
圆的半径和圆心的 x、y 坐标将作为参数传递给类的构造函数。
圆周上的点也认为是在圆中。
randPoint 返回一个包含随机点的x坐标和y坐标的大小为2的数组。
示例 1：

输入:
["Solution","randPoint","randPoint","randPoint"]
[[1,0,0],[],[],[]]
输出: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]
"""
import random
class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.center = (x_center, y_center)
        self.radius = radius

    def randPoint(self):
        # 矩形的原点坐标（最左下角的点）
        ractangle_x0 = self.center[0] - self.radius
        ractangle_y0 = self.center[1] - self.radius

        while True:
            # x,y是在矩形范围内随机生成的点的坐标
            x = ractangle_x0 + random.random() * 2 * self.radius
            y = ractangle_y0 + random.random() * 2 * self.radius

            # 假如x,y距离圆心得距离超过半径，说明点不在圆的范围以内
            if (self.center[0] - x) ** 2 + (self.center[1] - y) ** 2 <= self.radius ** 2:
                return [x, y]

# 思路 https://leetcode-cn.com/problems/generate-random-point-in-a-circle/solution/zai-yuan-nei-sui-ji-sheng-cheng-dian-by-leetcode/
# 代码：https://leetcode-cn.com/problems/generate-random-point-in-a-circle/solution/478-zai-yuan-nei-sui-ji-sheng-cheng-dian-by-haoyuh/

