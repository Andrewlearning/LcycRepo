"""
输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
"""

class Solution(object):
    def equals(self, sc, pc):
        for i in range(len(sc)):
            if sc[i] != pc[i]:
                return False
        return True

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or not p or len(s) < len(p):
            return []

        res = []
        sc = [0] * 26
        pc = [0] * 26

        # 先把pc，sc的hashmap给建好，并且先进行第一次比较
        for i in range(len(p)):
            sc[ord(s[i]) - ord("a")] += 1
            pc[ord(p[i]) - ord("a")] += 1

        if self.equals(sc, pc):
            res.append(0)

        # 然后我们继续比较，我们为了方便把P的长度先弄出来
        # 接下来就是有点滑动窗口的感觉了，在sc的表上操作
        # 把新进入窗口的元素记录在hashmap(i)
        # 把离开窗口的元素记录移除 hashmap[i-pLen]
        pLen = len(p)
        for i in range(pLen, len(s)):
            sc[ord(s[i]) - ord("a")] += 1
            sc[ord(s[i - pLen]) - ord("a")] -= 1

            if self.equals(sc, pc):
                res.append(i - pLen + 1)
        return res

"""
Time: O(n*k), Space: O(k)
https://algocasts.io/episodes/LPmwkomq
答案：
建立两个hashmap来代表两个字符串，然后我们把字符串中较短的那个串的长度，作为固定窗口的长度
每次比较两个固定窗口中所包含元素的数量和种类是否相同
"""