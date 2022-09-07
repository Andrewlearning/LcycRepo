"""
假设你是一位顺风车司机，车上最初有capacity个空座位可以用来载客。由于道路的限制，
车只能向一个方向行驶（也就是说，不允许掉头或改变方向，你可以将其想象为一个向量）。

这儿有一份乘客行程计划表trips[][]，
其中trips[i] = [num_passengers, start_location, end_location]包含了第 i 组乘客的行程信息：
必须接送的乘客数量；
乘客的上车地点；
乘客的下车地点。

输入：trips = [[2,1,5],[3,3,7]], capacity = 4
输出：false

请你根据给出的行程计划表和车子的座位数，来判断你的车是否可以顺利完成接送所用乘客的任务（当且仅当你可以在所有给定的行程中接送所有乘客时，返回true，否则请返回 false）。
"""
class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        points = []
        # 我们希望在到同一个位置的时候，乘客先下车，再上车
        # 所以把下车的值设为负，这样后面points在排序的时候就会被排到前面，方便我们处理
        for num, start, end in trips:
            points.append([start, num])
            points.append([end, -num])

        points.sort()
        curCap = 0

        for p in points:
            # 说明乘客需要上车，当前车上人数增加
            if p[1] > 0:
                curCap += abs(p[1])
            # 说明乘客需要下车，当前车上人数减少
            if p[1] < 0:
                curCap -= abs(p[1])

            # 假如当前车上人数 > 汽车容量，则不行
            if curCap > capacity:
                return False

        return True




