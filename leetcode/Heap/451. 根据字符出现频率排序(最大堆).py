"""
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

示例 1:

输入:
"tree"

输出:
"eert"

解释:
'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
"""


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 0:
            return s

        # 统计字符串的频率
        count = {}
        for char in s:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1

        # 制作最大堆，放char和频率
        maxheap = []
        for char in count:
            heapq.heappush(maxheap, (-count[char], char))

        # 把结果加到res
        res = ""
        for _ in range(len(maxheap)):
            tuple = heapq.heappop(maxheap)
            times = -tuple[0]
            char = tuple[1]
            res += char * times

        return res

"""
时间复杂度: O(Nlogk)
空间复杂度：O(N)
和692一样
"""