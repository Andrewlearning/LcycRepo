"""
给定二维空间中四点的坐标，返回四点是否可以构造一个正方形。

一个点的坐标（x，y）由一个有两个整数的整数数组表示。

示例:

输入: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
输出: True
"""

class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        points = [p1, p2, p3, p4]
        distance = []
        # 获得正方形4条边，以及两条对边的长度
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance.append(self.getDist(points[i], points[j]))

        distance.sort()

        # 假如有距离为0，说明有点重合，构不成正放心
        if distance[0] == 0:
            return False

        # 正方形是四条外边相等，两条对边也相等。这样才不会构成菱形
        return distance[0] == distance[1] and distance[1] == distance[2] and distance[2] == distance[3] and distance[
            4] == distance[5]

    def getDist(self, p1, p2):
        dx = p1[0] - p2[0]
        dy = p1[1] - p2[1]
        return dx ** 2 + dy ** 2

# https://www.acwing.com/video/2083/