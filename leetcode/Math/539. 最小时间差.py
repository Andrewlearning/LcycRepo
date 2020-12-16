class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        res = sys.maxsize
        t = []
        for c in timePoints:
            h, m = c.split(':')
            t.append(60 * int(h) + int(m))

        t.sort()

        for i in range(1, len(t)):
            res = min(res, t[i] - t[i - 1])

        # 处理23:54 和 1:10 的差这种情况，算24:00 - 23:53 + 1:10 - 0:00
        res = min(res, 24 * 60 - t[-1] + t[0])

        return res

# https://www.acwing.com/video/1997/