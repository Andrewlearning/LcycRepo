import heapq
class Solution(object):
    def minimumEffortPath(self, hs):
        """
        :type hs: List[List[int]]
        :rtype: int
        """
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # res[i,j] 表示 (0,0) -> (i,j) 的最小高度差
        res = [[float("inf")] * len(hs[0]) for i in range(len(hs))]
        res[0][0] = 0

        # (从起点到[curi, curj]位置的最小高度差, curi, curj)
        heap = [(0, 0, 0)]

        # 去过了的路径就不再去了
        visited = set()

        while heap:
            # curd 代表当当前路径的堆中最小值
            curd, curi, curj = heapq.heappop(heap)

            # 假如该节点被遍历过，则跳过
            if (curi, curj) in visited:
                continue
            visited.add((curi, curj))

            # 到达终点了，跳出循环
            if curi == (len(hs) - 1) and curj == (len(hs[0]) - 1):
                break

            for dir in dirs:
                newi = curi + dir[0]
                newj = curj + dir[1]
                if 0 <= newi < len(hs) and 0 <= newj < len(hs[0]):
                    # 更新从 (0,0) -> (newi, newj) 的最大高度差
                    newd = max(curd, abs(hs[newi][newj] - hs[curi][curj]))

                    # 假如新 (0,0) -> (newi, newj)的最大高度差 <  原来(0,0) -> (newi, newj)的最大高度差
                    # 则更新记录，并把这条路径放入到heapq中
                    # 我们希望，每次push进heap中的，都是局部最佳的答案
                    if newd <= res[newi][newj]:
                        res[newi][newj] = newd
                        heapq.heappush(heap, (newd, newi, newj))

        return res[-1][-1]

"""
我们可以从起点开始搜索邻近节点，计算出到达每一个点需要的最小体力值，同时利用优先级队列，确定下一个需要搜索的点。
https://leetcode-cn.com/problems/path-with-minimum-effort/solution/1631-dui-zui-xiao-ti-li-xiao-hao-lu-jing-j7ae/
"""