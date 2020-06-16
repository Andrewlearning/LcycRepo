"""
给定一个数组，将其划分成 M 份，使得每份元素之和最大值最小，每份可以任意减去其中一个元素。

输入：time = [1,2,3,3], m = 2
输出：3
解释：第一天小张完成前三题，其中第三题找小杨帮忙；第二天完成第四题，并且找小杨帮忙。这样做题时间最多的一天花费了 3 的时间，并且这个值是最小的。

示例 2：
输入：time = [999,999,999], m = 4
输出：0
解释：在前三天中，小张每天求助小杨一次，这样他可以在三天内完成所有的题目并不花任何时间。
"""
import sys
class Solution(object):
    def minTime(self, times, m):
        """
        :type time: List[int]
        :type m: int
        :rtype: int
        """
        # 这里的左边界要定为0，因为有可能要筛掉我们所选择的最大值要被筛选掉
        # 所以在这里不和440 一样
        l = 0
        r = sum(times)
        res = sys.maxsize

        while l <= r:
            mid = (l+r) // 2
            # 区间和
            sub_sum = 0
            # 按照当前mid，总共能分几个区间
            count = 1
            # 当前区间的最大值
            interal_max = 0

            for time in times:
                # 寻找当前区间内的最大值，因为待会我们要把它给剔除
                interal_max = max(interal_max, time)
                sub_sum += time

                # 假如说剔除了当前区间里的最大值，但是依然到达了超过阈值
                # 那么我们开始进行下一个区间的统计
                if sub_sum - interal_max > mid:
                    count += 1
                    sub_sum = time
                    interal_max = time

            if count <= m:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res


# 作者：kinger-2
# 链接：https://leetcode-cn.com/problems/xiao-zhang-shua-ti-ji-hua/solution/er-fen-sou-suo-shuang-bai-tong-guo-by-kinger-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


