import heapq
class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # 记录了从(0,0) -> 每个(x,y) 的最小高度差
        record = [[float("inf")] * len(heights[0]) for i in range(len(heights))]
        record[0][0] = 0

        # (从起点到[curi, curj]位置的最小高度差, curi, curj)
        heap = []
        heap.append((0, 0, 0))

        # 去过了的路径就不再去了
        visited = set()

        while heap:
            # curd 代表当当前路径的堆中最小值
            curd, curi, curj = heapq.heappop(heap)
            # print(curd, (curi, curj))
            # print(record[0])
            # print(record[1])
            # print(record[2])
            # print("\n")

            if (curi, curj) in visited:
                continue

            # 到达终点了，跳出循环
            if curi == (len(heights) - 1) and curj == (len(heights[0]) - 1):
                break

            visited.add((curi, curj))
            for dir in dirs:
                newi = curi + dir[0]
                newj = curj + dir[1]
                if 0 <= newi < len(heights) and 0 <= newj < len(heights[0]):
                    # 更新从 (0,0) -> (newi, newj) 的最大高度差
                    newd = max(curd, abs(heights[newi][newj] - heights[curi][curj]))

                    # 假如新 (0,0) -> (newi, newj)的最大高度差 <  原来(0,0) -> (newi, newj)的最大高度差
                    # 则更新记录，并把这条路径放入到heapq中
                    if newd <= record[newi][newj]:
                        record[newi][newj] = newd
                        heapq.heappush(heap, (newd, newi, newj))

        return record[-1][-1]

"""
我们可以从起点开始搜索邻近节点，计算出到达每一个点需要的最小体力值，同时利用优先级队列，确定下一个需要搜索的点。
https://leetcode-cn.com/problems/path-with-minimum-effort/solution/1631-dui-zui-xiao-ti-li-xiao-hao-lu-jing-j7ae/
"""