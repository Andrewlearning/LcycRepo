from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        nw = len(words[0])
        n = len(s)
        wmap = Counter(words)
        res = []

        for i in range(nw):
            l = i
            r = i

            # 滑动窗口
            window = Counter()

            # 只要没有越界，持续移动指针，因为right指向的是匹配的单词的下一位，所以这里需要=
            while r + nw <= n:
                curWord = s[r: r+nw]
                window[curWord] += 1
                r += nw

                # 出
                # 如果数量超过了目标数量，移动左边界
                while window[curWord] > wmap[curWord]:
                    window[s[l:l + nw]] -= 1
                    l += nw

                if r - l == nw * len(words):
                    res.append(l)

        return res