import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 最小堆，堆顶元素是堆里面最小的元素
        minHeap = []

        for num in nums:
            heapq.heappush(minHeap, num)

            # 始终维护堆的大小为k， 这样堆顶元素就是第K大的元素
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0]


"""
https://algocasts.io/episodes/vkmelbWb
Time: O(n*log(k)), Space: O(k)
"""