"""
给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

如果数组元素个数小于 2，则返回 0。

示例 1:

输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
"""
import sys
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 2:
            return 0

        # 找出所有数字中的最大值以及最小值
        minima = min(nums)
        maxima = max(nums)

        # 出现1 1 1的情况
        if minima == maxima:
            return 0

        # 桶的间距等于 (最大值-最小值)//(长度-1)
        margin = max(1, (maxima - minima) // (len(nums) - 1))

        # 桶的个数等于 (最大值-最小值)//间距 + 1
        bkt_size = (maxima - minima) // margin + 1

        # 初始化每个桶的最大值最小值
        bkt_min = [sys.maxsize] * bkt_size
        bkt_max = [0] * bkt_size

        for num in nums:
            # 每个数字它所被放在哪个桶里，用(值 - 最小值) // 桶间距 得到下标
            idx = (num - minima) // margin

            # 放进去后更新桶的最大值最小值
            bkt_min[idx] = min(bkt_min[idx], num)
            bkt_max[idx] = max(bkt_max[idx], num)

        # lastBktIdx指向上一个有元素的桶，因为中间有可能出现空桶
        res = lastBktIdx = 0

        for i in range(1, bkt_size):
            # 桶里的最大最小值并没进行过改变，说明桶里没有元素，跳过
            if bkt_min[i] == sys.maxsize and bkt_max[i] == 0:
                continue

            # res = 当前桶的最小值 - 上个桶的最大值，得到相邻元素间的最大差值
            res = max(res, bkt_min[i] - bkt_max[lastBktIdx])
            lastBktIdx = i
        return res

"""
答案来源：https://leetcode-cn.com/problems/maximum-gap/solution/164zui-da-jian-ju-tong-pai-xu-by-imkk/
思路来源：https://leetcode-cn.com/problems/maximum-gap/solution/tong-pai-xu-by-powcai/
"""
