class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if not s:
            return []
        if s in memo:
            return memo[s]

        # 当前s 所能产生的合法单词组合
        res = []

        for word in wordDict:
            # 当前单词无法匹配到s上
            if s.startswith(word) == False:
                continue
            # base case，只有一个单词的时候
            if s == word:
                res.append(s)
            else:
                # 获得更短s的拼接结果
                restOfres = self.helper(s[len(word):], wordDict, memo)
                # 当前单词 + 更短s拼接
                for item in restOfres:
                    temp = word + " " + item
                    res.append(temp)

        # 把当前字符串s所能构成的所有结果给保存起来，留给更长的s去使用
        memo[s] = res

        # 返回当前s 所能产生的合法单词组合
        return res

"""
这题已经不是我们前面看的那种简单的回溯了。也不能套用前面那些回溯的模版
https://www.youtube.com/watch?v=JqOIRBC0_9c
https://leetcode.com/problems/word-break-ii/discuss/44311/Python-easy-to-understand-solution
"""