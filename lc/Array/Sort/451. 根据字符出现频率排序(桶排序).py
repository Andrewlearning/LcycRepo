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
import collections


class Solution(object):
    def frequencySort1(self, s):
        # 记录每个字符出现的次数
        hashmap = collections.defaultdict(int)
        for i in range(len(s)):
            hashmap[s[i]] += 1

        bucket = collections.defaultdict(list)
        # bucket key=字符出现的次数 value:[有哪些字符出现这么多次]
        for key in hashmap.keys():
            freq = hashmap[key]
            bucket[freq].append(key)

        res = ""
        # 从大到小遍历字符可能出现的次数，这样会把出现最多次数的字符优先拼接
        for i in range(len(s), -1, -1):
            if bucket[i]:
                for c in bucket[i]:
                    res += c * i

        return res

"""
# O(n+k) 古城算法 这个做法比较好，桶排序
# https://www.bilibili.com/video/BV1G54y1a7gS
"""

class Solution(object):
    def frequencySort2(self, s):
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
