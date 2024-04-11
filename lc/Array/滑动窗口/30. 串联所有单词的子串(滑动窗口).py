"""
You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word in words
exactly once and without any intervening(介于中间的) characters.


Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting（开始坐标） at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
"""


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import Counter
        if not s or not words:
            return []

        nw = len(words[0])
        n = len(s)
        wmap = Counter(words)
        res = []

        """
        s = "barfoothefoobarman", words = ["foo","bar"]
        我们只遍历一个单词的长度是在于，因为我们都是按照 len(words) 为一组遍历
        从b -> (b)arf开始遍历  和从f -> bar(f)开始遍历，对于要遍历整个字符串而言都是一样的
        除了从f遍历会少遍历前面的bar以外，所以我们可以只遍历一个单词的长度
        """
        # 我们只遍历一个单词的长度是在于
        for i in range(nw):
            # 创建滑动窗口
            window = Counter()
            # 窗口的左右边界
            l = i
            r = i

            # 只要没有越界，持续移动指针，因为right指向的是匹配的单词的下一位，所以这里需要=
            while r + nw <= n:
                curWord = s[r: r + nw]
                window[curWord] += 1
                r += nw

                # 如果窗口里的所需单词数量超过了目标数量，移动左边界，去除单词
                while window[curWord] > wmap[curWord]:
                    window[s[l:l + nw]] -= 1
                    l += nw

                # 假如窗口长度 = 所需单词连在一起的长度
                # 且走到这里时，说明所需单词数量<=目标数量
                # 则说明当前window里的单词和数量 与我们的目标一致
                if r - l == nw * len(words):
                    res.append(l)

        return res

"""
借鉴acwing的思想，但是代码没有按照他的写
time:O(n**2) space O(n)
答案：
以单词长度切片 + 滑动窗口 + hashmap
"""


