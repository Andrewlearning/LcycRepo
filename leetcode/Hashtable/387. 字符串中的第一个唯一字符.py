"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
Examples:

s = "leetcode"
return 0.
s = "loveleetcode",
return 2.
"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1

        hashmap = {}

        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 1
            else:
                hashmap[s[i]] += 1

        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i

        return -1


"""
利用了hash map
https://algocasts.io/episodes/Y9pJkYWA
"""
        
        
        

