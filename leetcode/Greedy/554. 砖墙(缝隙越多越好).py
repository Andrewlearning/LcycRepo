"""
你的面前有一堵矩形的、由多行砖块组成的砖墙。 这些砖块高度相同但是宽度不同。你现在要画一条自顶向下的、穿过最少砖块的垂线。

砖墙由行的列表表示。 每一行都是一个代表从左至右每块砖的宽度的整数列表。

如果你画的线只是从砖块的边缘经过，就不算穿过这块砖。你需要找出怎样画才能使这条线穿过的砖块数量最少，并且返回穿过的砖块数量。

你不能沿着墙的两个垂直边缘之一画线，这样显然是没有穿过一块砖的。
"""
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        # x值：在该x值出现缝隙的次数
        lookup = collections.defaultdict(int)
        row = len(wall)
        for i in range(row):
            cur = 0
            for j in range(len(wall[i]) - 1):
                # 每块砖加完，那个值就是一个缝隙
                cur += wall[i][j]
                lookup[cur] += 1

        # 看最多一个x有多少缝隙
        maxGap = 0
        for value in lookup.values():
            if value > maxGap:
                maxGap = value

        return row - maxGap

# 链接：https://leetcode-cn.com/problems/brick-wall/solution/zhao-bian-jie-by-powcai/
