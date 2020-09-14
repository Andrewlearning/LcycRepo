class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # key: 状态  value:状态所对应的下标
        hashmap = {0: -1}
        vowels = "aeiou"

        # 00000， 用来记录子序列的 元音奇偶状态
        state = 0
        res = 0

        for i in range(len(s)):

            # 假如说vowels不存在 s[i], find()会返回-1
            j = vowels.find(s[i])

            # 假如说当前字母是元音字母
            if j >= 0:
                # 那么我们把 它的状态，在state里改变一下
                state ^= 1 << j

            # 假如说当前状态，不再hashmap里面的话
            # 记录当前状态和对应的下标
            if state not in hashmap:
                hashmap[state] = i

            # 假如一个状态出现两次，那么说明肯定有元音字符成对出现了
            # 例如 "l" 00000  "le" 01000  "lee" 00000
            # 我们发现 "l" 和 "lee" 的状态是一样的，这时表现了字符串里面出现了，"ee"这样的元音字符
            res = max(res, i - hashmap[state])

        return res

"""
https://www.youtube.com/watch?v=tAlQxFvak2U
"""
