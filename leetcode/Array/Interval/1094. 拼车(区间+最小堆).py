"""
假设你是一位顺风车司机，车上最初有 capacity 个空座位可以用来载客。由于道路的限制，
车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向，你可以将其想象为一个向量）。

这儿有一份乘客行程计划表 trips[][]，
其中 trips[i] = [num_passengers, start_location, end_location] 包含了第 i 组乘客的行程信息：
必须接送的乘客数量；
乘客的上车地点；
乘客的下车地点。

输入：trips = [[2,1,5],[3,3,7]], capacity = 4
输出：false

请你根据给出的行程计划表和车子的座位数，来判断你的车是否可以顺利完成接送所用乘客的任务（当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false）。
"""
import heapq
class Solution:
    def carPooling(self, trips, capacity):

        # 先按照乘客的上车地点，从小到大排序
        trips.sort(key=lambda x: x[1])

        # 最小堆[下车地点，乘客人数]
        off_dist = []

        #乘客人数
        count = 0

        for i in range(len(trips)):
            # 上车地点
            dist = trips[i][1]

            # 这一个乘客上车地点是否 > 上一个乘客的下车地点，是的话上一波乘客可以下车
            while off_dist and dist >= off_dist[0][0]:
                _, passenger = heapq.heappop(off_dist)
                # 成功下车
                count -= passenger

            # 这一波乘客可以上车
            count += trips[i][0]

            #看看这波乘客上车后，车坐不坐得下
            if count > capacity:
                return False

            # 一切顺利的话那我们把这一波乘客的下车地点 和人数放进最小堆里
            heapq.heappush(off_dist, [trips[i][-1], trips[i][0]])
        return True


"""
主体思路和253.会议室2一样，只不过问题变得稍微再复杂一点点

https://leetcode-cn.com/problems/car-pooling/solution/pin-che-by-xxbryce/
还有一种更简单的方法，但是不是通式通解，所以不放
"""

