"""
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:

可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
示例 1:

输入: [ [1,2], [2,3], [3,4], [1,3] ]

[1-----2]
[1--------------3]
      [2--------3]
               [3---------4]


输出: 1, 移除[1,3]
"""


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals and len(intervals) == 0:
            return 0

        # 按照区间的结束来进行从小到大排序
        intervals.sort(key=lambda x: x[1])

        # 所有的区间的数量
        lenIntervals = len(intervals)

        # 不重叠区间的数量
        disconnect = 1

        # 第一个区间
        cur = intervals[0]

        for i in range(1, len(intervals)):
            # 当发现两个区间不重叠的时候，disconnect += 1, 更新cur
            if cur[1] <= intervals[i][0]:
                disconnect += 1
                cur = intervals[i]


        # 所有区间 - 不重叠区间 = 重叠区间的数量
        return lenIntervals - disconnect


"""
解题思路
把问题转换成：最多能选取几个区间不重叠的区域
那答案显然变成：总区间个数 - 不重叠区间个数

这题一个难点，为什么要 按照end的大小来排序: 因为我们每次找出的都是当前最小的end, 然后再把end 前的清除

正确的思路其实很简单，可以分为以下三步：
1.从区间集合 intvs 中选择一个区间 x，这个 x 是在当前  &&& 所有区间中结束最早的（end 最小) &&&&
2.把所有与 x 区间相交的区间从区间集合 intvs 中删除。
3.重复步骤 1 和 2，直到 intvs 为空为止。之前选出的那些 x 就是最大不相交子集。

把这个思路实现成算法的话，可以按每个区间的 end 数值升序排序，因为这样处理之后实现步骤 1 和步骤 2 都方便很多:

作者：labuladong
链接：https://leetcode-cn.com/problems/non-overlapping-intervals/solution/tan-xin-suan-fa-zhi-qu-jian-diao-du-wen-ti-by-labu/





按头排序不行的例子

[[1,100],[11,22],[1,11],[2,12]]
本题应该删除[1,100],[2,12]

按start排
[1---------------------------100]
[1-------11]
   [2---------12]
         [11---------22]
         

按end排
[1-------11]
   [2---------12]
         [11---------22]
[1---------------------------100]

"""