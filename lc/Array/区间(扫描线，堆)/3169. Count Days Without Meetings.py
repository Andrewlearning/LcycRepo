"""
You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).

Return the count of days when the employee is available for work but no meetings are scheduled.

Input: days = 10, meetings = [[5,7],[1,3],[9,10]]
Output: 2
Explanation:
There is no meeting scheduled on the 4th and 8th days.
"""


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        n = len(meetings)
        meetings.sort()
        m = meetings
        res = 0

        # 我们用这种做法， 就可以计算出头部和第一个区间之间的差值了
        r = 0
        for i in range(n):
            cur = m[i]
            if cur[0] > r:
                res += cur[0] - r - 1

            # 更行r值
            if cur[1] > r:
                r = cur[1]

        res += days - r
        return res

# 答案参考自 https://leetcode.cn/problems/count-days-without-meetings/solutions/2798222/pai-xu-by-tsreaper-o07o/

# 我在周赛写的答案
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        n = len(meetings)
        meetings.sort(key=lambda x: x[0])
        m = meetings
        res = 0

        first = float('inf')
        last = -1

        curEnd = m[0][1]
        for i in range(n - 1):
            cur = m[i]
            if cur[1] > curEnd:
                curEnd = cur[1]
            nxt = m[i + 1]

            diff = nxt[0] - curEnd
            if diff > 1:
                res += diff - 1

            first = min(first, cur[0], nxt[0])
            last = max(last, cur[1], nxt[1])

        if n == 1:
            first = m[0][0]
            last = m[0][1]
        res += (days - last) + (first - 1)
        if res == float('inf'):
            return 0

        return res