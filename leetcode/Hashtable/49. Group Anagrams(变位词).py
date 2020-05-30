"""
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
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

        # key:每个字母出现的次数  value:一个装单词的list
        hashmap = {}

        for string in strs:
            key = self.getKeybyCount(string)
            if key in hashmap:
                hashmap[key].append(string)
            else:
                hashmap[key] = [string]

        return [value for value in hashmap.values()]

    # 把每个单词所对应的hash给记录下来
    def getKeybyCount(self, string):
        table = [0] * 26
        for char in string:
            table[ord(char) - ord("a")] += 1

        return str(table)


"""   
Time: O(n*k)
https://algocasts.io/episodes/vkmerKGb
"""