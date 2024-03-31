"""
给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。

示例:

输入:
[[0,0],[1,0],[2,0]]

输出:
2

解释:
两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
"""


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        res = 0

        for i in range(len(points)):
            # 每次以第i个元素为中心，测算其他店到i的距离
            hashmap = collections.defaultdict(int)
            for j in range(len(points)):
                if i != j:
                    dx = points[i][0] - points[j][0]
                    dy = points[i][1] - points[j][1]
                    dist = dx * dx + dy * dy
                    hashmap[dist] += 1

            # 假如说存在两个或以上的点到i的距离相等，那么他们可以构成回形标
            # 然后计算方法用排列来算，因为相同元素不同位置也是算一种情况
            for key in hashmap.keys():
                dis_count = hashmap[key]
                res += dis_count * (dis_count - 1)

        return res

# https://www.acwing.com/video/1847/