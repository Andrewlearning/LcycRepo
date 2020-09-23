class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0

        self.m = len(heightMap)
        self.n = len(heightMap[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        self.visited = set()
        minheap = []
        res = 0

        for i in range(self.m):
            for j in range(self.n):
                # 把四周围一圈的都放进最小堆里去
                if i == 0 or j == 0 or i == self.m - 1 or j == self.n - 1:
                    heapq.heappush(minheap, (heightMap[i][j], i, j))
                    self.visited.add((i, j))

        print(minheap)

        while minheap:
            # 把值最小的最先pop出来
            bar = heapq.heappop(minheap)

            for (dirx, diry) in dirs:
                next_x = bar[1] + dirx
                next_y = bar[2] + diry

                if self.valid(heightMap, next_x, next_y):
                    # 假如说新坐标 小于bar的高度，说明可以接水
                    # 假如说大于bar的高度， 说明不能接水
                    res += max(0, bar[0] - heightMap[next_x][next_y])

                    # 我们选取 bar[0] 和 heightMap[next_x][next_y]中比较大的那个放进heap中
                    # 作为当前坐标的最长板
                    # 后续减这个坐标的bar时，差就是深度
                    heapq.heappush(minheap, (max(bar[0], heightMap[next_x][next_y]), next_x, next_y))
                    self.visited.add((next_x, next_y))

        return res

    # 检查看next 是否合法
    def valid(self, heightMap, i, j):
        return 0 <= i < self.m and 0 <= j < self.n and (i, j) not in self.visited

"""
思路来源：https://www.bilibili.com/video/BV1jJ411W7ZJ?from=search&seid=4129032771053785766
写法来源：https://leetcode-cn.com/problems/trapping-rain-water-ii/solution/priority-queue-bfs-by-bugfree-e/

这题使用了 heap来跟踪最小高度的元素，每次都把高度最小的元素给pop出来
            然后用BFS来扩散，查找比四周小的格子

为什么这里要用heap呢，因为他是起一个追踪作用
一开始我们先挑一个最矮的出来，然后BFS去扩散。
因为一开始我们找的点是最矮的，假如说扩散的都是比一开始高的，那么也该结束了，heap也不会继续扩散
                            假如说扩散的是比一开始矮的，那么heappop出就是这个更矮的，于是我们可以继续沿那个点扩散，res增加

所以heap起到的作用是， 假如说那一片都是可以盛水的，那么就会一直往那里扩散，
                    假如说那一片是不可以盛水的，那么就换个地方扩散
                    具体动画看思路来源

"""