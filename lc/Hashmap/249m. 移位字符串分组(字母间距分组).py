"""
给定一个字符串，对该字符串可以进行 “移位” 的操作，也就是将字符串中每个字母都变为其在字母表中后续的字母，比如："abc" -> "bcd"。这样，我们可以持续进行 “移位” 操作，从而生成如下移位序列：

"abc" -> "bcd" -> ... -> "xyz"
给定一个包含仅小写字母字符串的列表，将该列表中所有满足 “移位” 操作规律的组合进行分组并返回。

就是abc三个字母与字母之间的间距，与bcd字母与字母之间的间距是一样的
所以他们可以被归于一类
"""

import collections
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """

        hashmao = collections.defaultdict(list)

        for s in strings:
            key = ''
            for i in range(len(s) - 1):
                dist = (ord(s[i + 1]) - ord(s[i])) % 26
                key += str(dist)

            hashmao[key].append(s)

        return list(hashmao.values())

# https://leetcode-cn.com/problems/group-shifted-strings/solution/gou-jian-key-jin-xing-map-cao-zuo-by-moqimoqidea/


