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

        if sc == pc:
            res.append(0)

        pLen = len(p)
        for i in range(pLen, len(s)):
            # 右指针+= 1
            sc[ord(s[i]) - ord("a")] += 1

            # 左指针-= 1
            sc[ord(s[i - pLen]) - ord("a")] -= 1

            # 假如两个哈希表对的上，则append左指针的位置
            if sc == pc:
                res.append(i - pLen + 1)
        return res

"""
Time: O(n*k), Space: O(k)
https://algocasts.io/episodes/LPmwkomq
答案：
建立两个hashmap来代表两个字符串，然后我们把字符串中较短的那个串的长度，作为固定窗口的长度
每次比较两个固定窗口中所包含元素的数量和种类是否相同
"""