"""
Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), find the minimum number of conference rooms required.

For example
Given[[0, 30],[5, 10],[15, 20]],
return2.

给出事件所需要占用的事件，问我们最少需要用多少个会议室。[0，30]需要用一个
[[5,10],[15,20]]需要用一个
原文链接：https://blog.csdn.net/qq508618087/article/details/50762939
"""
import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[list[int]]
        :rtype: int
        """
        intervals.sort(key = lambda x:x[0])

        # heap表示，为满足会议需求，需要同时开多少个房间
        # 只记录每个房间的结束时间
        minheap = []

        for interval in intervals:

            # minheap[0]是最早的结束时间
            # 假如说 新会议开始时间 >= 老会议最早结束时间, 那说明可以共用一间房
            if minheap and interval[0] >= minheap[0]:
                heapq.heapreplace(minheap, interval[1])

            # 1.假如说 新会议开始时间 < 老会议最早结束时间，说明不能共用一间房，所以要push一个新房间的结束时间进去
            # 2.没有房间在被使用，这就不存在房间的共用了，所以要加房间
            else:
                heapq.heappush(minheap, interval[1])

        return len(minheap)

"""
这题的做法是，假如说在同一个时间段，有两个事件需要同时进行，那么就需要两个房间
要是他们的时间是间隔开的，那么只需要同一个房间
事件1：------------------
事件2:          -------------
事件3:                         ----------- 
所以我们只需要两个房间

答案：
https://leetcode-cn.com/problems/meeting-rooms-ii/solution/hui-yi-shi-ii-by-leetcode/
time O(nlogn) , space O(n)
"""