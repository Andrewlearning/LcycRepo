"""
就是区间合并
"""
n = int(input())
intervals = []
for i in range(n):
    intervals.append(list(map(int, input().split())))

intervals = sorted(intervals, key=lambda x: x[0])
res = []


for interval in intervals:
    if not res:
        res.append(interval)
    elif interval[0] <= res[-1][1]:
        res[-1][1] = max(res[-1][1], interval[1])
    else:
        res.append(interval)


print(len(res))
