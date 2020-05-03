"""
输入：tasks = ["A","A","A","B","B"], n = 2
输出：8
解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> 空槽补位.
     在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间
     而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。
"""

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # 一开始先把每个字母所对应的频率给加入到maxheap里面去
        maxheap = []
        for x in set(tasks):
            maxheap.append((-tasks.count(x), x))

        heapq.heapify(maxheap)


        time = 0

        # 当maxheap还有元素的时候，继续执行放置
        while len(maxheap) > 0:
            i = 0

            # temp用来记录我们每个被pop出去的字母，最后我们把它的次数-1后再加回到queue
            temp = []

            #首先先在优先队列中选择最多n+1个任务，把他们的数量减去1
            while i <= n:
                if len(maxheap) > 0:
                    # 当前字母的出现次数-1后依旧大于0，说明它依旧存在，把它加进temp
                    # 待会再把它重新添加进heap里面去
                    if -maxheap[0][0] > 1:
                        temp.append(maxheap.pop(0))
                    # 要是-1等于=0，的话，说明这个字母不能用了，直接pop掉
                    else:
                        maxheap.pop(0)

                # 这里有几个作用
                # 当heap还有元素时，每用一个元素 time++
                # 当heap已经没元素时，上面那个判断跳过，直接time++, 表示补空位
                time += 1

                # 当所有字母都用完的时候，我们直接跳出循环，返回结果
                if len(maxheap) == 0 and len(temp) == 0:
                    break

                i += 1



            # 把每个字母的次数-1后加回到heap里去
            for element in temp:
                heapq.heappush(maxheap, (element[0] + 1, element[1]))

        return time

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


