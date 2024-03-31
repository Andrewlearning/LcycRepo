"""
二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。

每个 LED 代表一个 0 或 1，最低位在右侧。
"""

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []

        for i in range(1 << 10):
            # 看我们穷举到i变成二进制有多少个1
            cur_one = 0

            # j用来数当前i有多少个1
            for j in range(10):
                if (i >> j) & 1 == 1:
                    cur_one += 1

            # 假如说当前i 的二进制位上的1，和num亮了多少盏灯一样的话
            # 我们就要判断这个当前i能不能构成合法时间了
            if cur_one == num:
                # 只有上面四盏灯才是小时
                hour = i >> 6
                # 下面六盏灯是分钟
                # 63 = 111111
                minute = i & 63

                # 看时间合不合法
                if hour < 12 and minute < 60:
                    res.append("%d:%02d" % (hour, minute))

        return res

# https://www.acwing.com/video/1797/