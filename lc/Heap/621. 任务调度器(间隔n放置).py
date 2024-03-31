"""
输入：tasks = ["A","A","A","B","B"], n = 2
输出：8
解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> 空槽补位.
     在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间
     而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。
"""
import heapq
from collections import defaultdict
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # 如果冷却时间为0，直接返回任务的数量，因为怎么执行任务都可以
        if n == 0:
            return len(tasks)

        # 统计每个任务的出现频率
        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1

        # 构建最大堆（使用负数表示最大堆）, 用于记录每个任务的出现频率
        maxHeap = []
        for freq in freq.values():
            heappush(maxHeap, -freq)

        res = 0

        while maxHeap:
            # 临时列表用于存储本次执行的任务
            temp = []

            # 我们相当于预留一个n+1的执行时间，在n+1这个时间段内，每种任务都只能运行一次
            # 假如在n+1这个周期内，任务数量不够，则需用idle来填充
            for _ in range(n + 1):
                # 如果堆不为空，取出堆顶任务并放入temp中，并减少一次任务需要运行的次数
                if maxHeap:
                    temp.append(heapq.heappop(maxHeap) + 1)
                # 假如堆为空，说明在当前n+1个时间段内已经没有任务可以执行了(因为两相同任务执行间隔最小为n)
                # 要使用idle来进行填充不用执行任务的间隔

            for t in temp:
                # 如果任务频率小于0，表示任务还未执行完毕，需要重新放入堆中，在下一个循环中继续执行
                if t < 0:
                    heapq.heappush(maxHeap, t)

            # 根据堆里是否还有任务需要执行，来判断本次循环CPU执行了多少次interval
            # 如果堆不为空，增加n+1个周期，因为说明本次循环n+1的时间被完全利用
            # 如果堆为空，则表示所有任务已经执行完毕，不需要再统计idle的时间
            if maxHeap:
                res += n + 1
            else:
                res += len(temp)

        return res

"""
本题有巧妙的数学解法，但是我选择使用比较具有通用性的解法，这种解法是767的迁移

时间复杂度：O(time)，由于我们给每个任务都安排了时间
因此时间复杂度和最终的答案成正比。
空间复杂度：O(1)。
理解题意：https://www.bilibili.com/video/BV1Wt411Y7Y9?from=search&seid=611897316854036001
解法：https://leetcode-cn.com/problems/task-scheduler/solution/ren-wu-diao-du-qi-by-leetcode/

算法：
在选择每一轮中的任务时，我们也可以用优先队列（堆）来代替排序。
在一开始，我们把所有的任务加入到优先队列中。
在每一轮，我们从优先队列中选择最多 n + 1 个任务，把它们的数量减去 1，再放回堆中（如果数量不为 0），直到堆为空。

"""


