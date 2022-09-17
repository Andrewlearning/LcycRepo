"""
冬季已经来临。你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。

在加热器的加热半径范围内的每个房屋都可以获得供暖。

现在，给出位于一条水平线上的房屋houses 和供暖器heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。

说明：所有供暖器都遵循你的半径标准，加热的半径也一样。


示例 1:

输入: houses = [1,2,3], heaters = [2]
输出: 1
解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
示例 2:

输入: houses = [1,2,3,4], heaters = [1,4]
输出: 1
解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
"""

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        # 先对两个数组进行排序，因为代表着位置
        self.houses = sorted(houses)
        self.heaters = sorted(heaters)

        # l,r代表暖气的供暖范围
        l = 0
        r = 10 ** 9

        while l < r:
            # mid 代表暖气的供暖范围
            mid = (l + r) // 2

            # 假如说mid这个供暖范围所需要的供暖器数量 <= 实际有的供暖器数量
            # 说明供暖器的范围 >= 目标供暖器的值，我们希望得到它的左边界
            # 我们的供暖范围太大了，得缩小点
            if self.count(mid) <= len(self.heaters):
                r = mid
            # 假如mid不行的话，找比l大的供暖范围
            else:
                l = mid + 1

        return r

    def count(self, mid):
        # j代表指向heater的指针
        j = 0
        for i in range(len(self.houses)):
            # 假如房子与暖气的距离大于供暖距离，那么说明当前暖气不能给房子i供暖
            # 要移动到下一个暖气
            while j < len(self.heaters) and abs(self.houses[i] - self.heaters[j]) > mid:
                j += 1
        # 总共使用了j + 1个供暖器
        return j + 1

# https://www.acwing.com/video/1883/