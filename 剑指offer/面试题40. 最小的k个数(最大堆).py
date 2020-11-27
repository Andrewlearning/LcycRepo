import heapq
class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not arr or k == 0:
            return []

        heap = []

        for num in arr:

            if len(heap) < k:
                heapq.heappush(heap, -num)
            else:
                # 为什么我们不直接heapreplace呢
                # 因为有可能发生 0 与 -3，的情况。 按照我我们的需求，我们肯定是要0， 因为0比3小
                # 但是按照我们需要的heapq来看， -3会把0给顶掉
                # 换而言之，除0意外的所有情况都是适用的，但我们需要对0进行特殊处理
                if -heap[0] > num:
                    heapq.heapreplace(heap, -num)

        return [-num for num in heap]


"""
我们可以用最大堆来做
因为当我们发现 有元素 < 堆顶元素的时候， 就把堆顶元素给拿掉
所以就导致了 最后留在长度k的heap里面的数字，都是最小的k个数字

满足了我们所需要的要求
"""