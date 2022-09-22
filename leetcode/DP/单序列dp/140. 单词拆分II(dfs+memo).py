class Solution(object):
    def wordBreak(self, s, wordDict):
        self.words = set(wordDict)
        self.mem = {}
        return self.helper(s, wordDict)

    def helper(self, s, wordDict):
        # 假如我们已经记录过字符串s 所对应的答案组合，那么直接返回
        if s in self.mem:
            return self.mem[s]

        res = []
        # 1. 假如一串s在 words里面，那么把它先记录为答案
        if s in self.words:
            res.append(s)

        # 2. 分割s成两部分，来递归求解潜在的合法分割组合
        for i in range(1, len(s)):
            # 分割出单词 s[i:-1]
            right = s[i:]

            # 假如这个分割不成立，那后面也不用看了
            if right not in self.words:
                continue

            # 假如分割成立，那么继续对s[0:i-1]进行分割，得到s[0:i-1]分割的答案组合
            for w in self.helper(s[0:i], wordDict):
                # 拼接 s[0:i-1]所产生的答案组合 和 s[i:-1]的答案
                res.append(w + " " + right)

        # 记录当前字符串s 和所对应的答案组合
        self.mem[s] = res
        return res

"""
这题已经不是我们前面看的那种简单的回溯了。也不能套用前面那些回溯的模版
https://www.youtube.com/watch?v=JqOIRBC0_9c
http://zxi.mytechroad.com/blog/leetcode/leetcode-140-word-break-ii/
"""