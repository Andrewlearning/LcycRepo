"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        # key:每个字母出现的次数  value:一个装单词的list
        m = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            m[str(key)].append(s)

        return m.values()


"""   
时间复杂度：O(n * k)，其中 n 是字符串的数量，k 是字符串的最大长度。我们不再需要排序，而是使用计数方法。
空间复杂度：O(n * 26)，即 O(n)。虽然我们为每个字符串创建了一个长度为 26 的数组，但这个长度是固定的，不随输入增大而增大。
"""