class Solution:
    def findRightInterval(self, intervals):
        n = len(intervals)

        # 排序前给每一项的末尾添加索引
        for i in range(n):
            intervals[i].append(i)

        # 按区间头的大小进行排序
        intervals.sort(key=lambda x: x[0])

        # 储存每个区间的最接近右区间
        res = [-1] * n

        for i in range(n):
            # 二分搜索的区间，是在当前区间以后进行搜索
            l = i + 1
            r = n - 1

            # 当前区间的末尾比 最后一个区间的头还要大，说明当前区间无解
            if intervals[i][1] > intervals[r][0]:
                continue

            # 这里的二分查找，借用了34题的做法，这种二分查找是查找某个bound常用的
            # 在这里我们要找到离当前intervel最近的合法右区间
            index = -1
            while l <= r:
                mid = (l + r) // 2
                # mid 在一个合理的区间内, 所以这个mid不用排除, 我们用index来记录mid
                if intervals[i][1] <= intervals[mid][0]:
                    index = mid
                    r = mid - 1
                # intervals[i][1] > intervals[mid][0]
                # mid不满足条件，l = mid + 1
                else:
                    l = mid + 1

            # 更新这个intervel的最近右区间
            res[intervals[i][2]] = intervals[index][2]
        return res


# 思路： https://www.acwing.com/video/1838/
# 代码 https://leetcode-cn.com/problems/find-right-interval/solution/python-er-fen-dai-ma-jian-ji-by-zronghui/
