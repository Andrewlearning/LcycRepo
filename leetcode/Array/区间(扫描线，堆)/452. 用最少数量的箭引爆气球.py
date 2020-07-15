"""
给定气球的直径，求我们能最多一次射爆的量

输入:
[[10,16], [2,8], [1,6], [7,12]]

[1--------6]
  [2-------------8]
              [7-------------12]
                        [10--------16]

输出:
2

解释:
对于该样例，我们可以在x = 6（射爆[2,8],[1,6]两个气球）和 x = 11（射爆另外两个气球）。
"""
class Solution:
    def findMinArrowShots(self, points):
        if not points:
            return 0

        # 首先先针对气球的尾部进行排序
        points.sort(key=lambda x: x[1])

        arrows = 1
        first_end = points[0][1]

        for x_start, x_end in points:

            # 说明两个区间之间有gap， 所以需要多一支箭
            if first_end < x_start:
                arrows += 1

                # 有gap的话，我们更新最远的尾部，等于是换了一个区间，重新看有多少个区间在里面
                first_end = x_end

        return arrows

"""
时间复杂度：O(NlogN)。因为对输入数据进行了排序。
空间复杂度：O(1)，仅仅使用了常数空间。
https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/solution/yong-zui-shao-shu-liang-de-jian-yin-bao-qi-qiu-b-2/

"""