"""
You are given a 2D integer array items where items[i] = [pricei, beautyi] denotes the price and beauty of an item respectively.

You are also given a 0-indexed integer array queries. For each queries[j], you want to determine the maximum beauty of an item whose price is less than or equal to queries[j]. If no such item exists, then the answer to this query is 0.

Return an array answer of the same length as queries where answer[j] is the answer to the jth query.

Input: items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]
Output: [2,4,5,5,6,6]
"""
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        n = len(items)

        # 先用一个数组，记录从[0~i]这个范围内最大的beauty值
        maxPre = [0] * n
        for i in range(n):
            if i == 0:
                maxPre[i] = items[i][1]
            else:
                maxPre[i] = max(maxPre[i - 1], items[i][1])

        # 找出小与等于q的最右边元素
        def h(q):
            l = 0
            r = n - 1

            while l < r:
                mid = (l + r + 1) // 2

                if items[mid][0] <= q:
                    l = mid
                else:
                    r = mid - 1
            return l

        res = []
        for q in queries:
            # 假如query的值小于最小的beauty值，说明不存在这个元素
            if q < items[0][0]:
                res.append(0)
            # 否则我们找出当前query所对应的最大元素
            else:
                res.append(maxPre[h(q)])

        return res

# https://leetcode.com/problems/most-beautiful-item-for-each-query/discuss/1575973/Python3-sorting-%2B-binary-search