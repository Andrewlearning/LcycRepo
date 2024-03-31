class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        count = {}

        # 统计词频
        for word in words:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1

        # 把词频和单词一起装进最大堆
        maxheap = []
        for word in count:
            heapq.heappush(maxheap, (-count[word], word))

        # 返回前k个高频单词
        return [heapq.heappop(maxheap)[1] for _ in range(k)]


"""
https://leetcode-cn.com/problems/top-k-frequent-words/solution/qian-kge-gao-pin-dan-ci-by-leetcode/

时间复杂度：O(Nlogk)。其中 N 是 words 的长度。我们用 O(N) 的时间计算每个单词的频率，然后将 N 个单词添加到堆中，添加每个单词的时间为 O(logk) 。最后，我们从堆中弹出最多 k 次。因为 k <= N 的值，总共是 O(Nlogk)。
空间复杂度：O(N)，用于存储我们计数的空间

"""

