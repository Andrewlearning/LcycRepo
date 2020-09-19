"""
给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 h 指数。

h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）
    总共有 h 篇论文分别被引用了至少 h 次。（其余的 N - h 篇论文每篇被引用次数 不超过 h 次。）

例如：某人的 h 指数是 20，这表示他已发表的论文中，每篇被引用了至少 20 次的论文总共有 20 篇。

 示例：

输入：citations = [3,0,6,1,5]
输出：3
解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
     由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。
"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)

        # 制造一个 n+1 的桶
        bucket = [0] * (n + 1)

        for citation in citations:
            # 我们把大于等于桶长度的，都放在一个桶里面
            if citation >= n:
                bucket[n] += 1
            # 其他的都放在各自应该待的位置
            else:
                bucket[citation] += 1

        # >= 当前引用次数的论文数量
        cur = 0
        for i in range(n, -1, -1):
            cur += bucket[i]
            # cur数量的论文每篇被引用次数 至少为i次
            if cur >= i:
                return i

# time On, Space On
#  https://leetcode-cn.com/problems/h-index/solution/hzhi-shu-by-powcai/
