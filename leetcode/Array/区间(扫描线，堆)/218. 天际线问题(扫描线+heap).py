class Solution(object):
    def getSkyline(self, buildings):
        # 思路：最大堆，每次在判断关键点的时候，移除所有右端点≤当前点的堆顶。
        if not buildings: return []
        points = []

        # [高度，最右边]，我们必须预设一个虚拟值，提供给第一个while 循环去进行判断
        heap = [[0, float('inf')]]

        # 同样res也是, 给个初始值，为了给下面的做判断
        res = [[0, 0]]

        # 1.将所有端点加入到点集中(每个建筑物的左右端点)
        for l, r, h in buildings:
            # 放入左端点，这里负号将最小堆，排序的时候就会按照 左坐标排序，如果两个左坐标相同，高度小的优先
            points.append((l, -h, r))
            # r的右端的右边设为0
            points.append((r, h, 0))


        # 2.将端点从小到大排序
        points.sort()  # 如果当前点相等，则按照高度升序


        # 3.按坐标从左到右顺序遍历每一个点
        for l, h, r in points:

            # 当前方块的左坐标，已经超过最大堆堆顶元素的右坐标
            # 那么说明 最大堆的堆顶元素和当前方块已经不在一个范围内了，所以pop掉
            while l >= heap[0][1]:
                # 出堆：保证当前堆顶为去除之前建筑物右端点的最大值。
                heapq.heappop(heap)

            # 把左端元素入堆，因为左端元素的高度都为负
            if h < 0:
                heapq.heappush(heap, [h, r])

            # 拿上一个描的点的高度 与 当前heap最大值对比
            # 假如说不一样，说明出现了一个新点需要我们去描
            # 又因为堆里放的高度，全是左端点的，所以要加负号
            if res[-1][1] != -heap[0][0]:
                # 所以我们把 当前新的左端点坐标，以及高度放进去
                res.append([l, -heap[0][0]])

        # res一开始有个[0,0], 我们忽略掉
        return res[1:]

"""
n 是矩形数量
ime: O(n^2), Space: O(n)
https://algocasts.io/episodes/LPmwqNpq
思路来源，但是仿照写代码跑不通

代码来源：https://leetcode-cn.com/problems/the-skyline-problem/solution/python3-sao-miao-xian-zui-da-dui-wan-zheng-zhu-shi/

完整思路：

0.创建一个最大堆，专门用来存放 (高度，左端点），
    最大堆的作用是，在方块重叠部分，对最大高度起到一个筛选作用（因为我们只描最高点）

1. 我们把每个方块的左右端点，以及左右端点对应的高度，弄成一个对
    存进points里，然后对它进行一个排序，使得遍历的时候我们是从左往右遍历的

2. 然后我们遍历points里的每个点
    2.1 首先我们先把右坐标，小于当前点左坐标的点清除，因为我们线已经扫到了一个新的区间了，就不可能在之前的区间上描了
    2.2 然后我们把左端点入栈
    2.3 看新的左端点入栈后，是否产生一个新的高度，如果产生，那么我们就描一个新的点    
     
"""