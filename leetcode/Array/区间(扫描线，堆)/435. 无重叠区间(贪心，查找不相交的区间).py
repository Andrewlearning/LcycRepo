"""
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:

可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠, 这种情况不算有交集。
示例 1:

输入: [ [1,2], [2,3], [3,4], [1,3] ]

[1-----2]
[1--------------3]
      [2--------3]
               [3---------4]


输出: 1, 移除[1,3]
"""


class Solution(object):
    def eraseOverlapIntervals(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        if not nums and len(nums) == 0:
            return 0

        # 按照区间的结束来进行从小到大排序
        nums.sort(key=lambda x: x[1])

        # 所有的区间的数量
        lenIntervals = len(nums)

        # 不重叠区间的数量
        disconnect = 1

        # 第一个区间
        cur = nums[0]

        for i in range(1, len(nums)):
            # 尽可能选择没有重叠的区间，那么没有被选的区间就说明他们导致了重叠
            # 当发现两个区间不重叠的时候，disconnect += 1, 更新cur
            if cur[1] <= nums[i][0]:
                disconnect += 1
                cur = nums[i]


        # 所有区间 - 不重叠区间 = 重叠区间的数量
        return lenIntervals - disconnect


"""
435和452是同一道题，都是通过查找有多少个区间不重叠来解题

解题思路
把问题转换成：最多能选取几个区间不重叠的区域
那答案显然变成：总区间个数 - 不重叠区间个数

解题过程
1. 先把所有区间按照尾端点进行排序
2. 然后从第一个区间的尾端点开始往后看，看有没有覆盖到其他区间，覆盖到其他区间则跳过
当碰到覆盖不到的区间，则记录，并移动到下一个区间继续看

这题一个难点，为什么要 按照end的大小来排序: 因为我们每次找出的都是当前最小的end, 然后再把end 前的清除
贪心证明思路: https://www.acwing.com/video/1835/





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