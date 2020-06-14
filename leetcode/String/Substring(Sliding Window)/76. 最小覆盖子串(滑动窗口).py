"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
这个题目说的是，给你两个字符串 s 和 t，你要在 s 中找到一个最短子串，
它包含 t 中所有的字符。如果找不到满足条件的子串，就返回空字符串。
"""

from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        # l,r是滑动窗口的[l,r]
        left, right = 0, 0

        # 最小子串开始的下标， 和子串的最小长度
        start, length = 0, len(s) + 1

        # 里面放着滑动窗口 还需要多少字母(数量)
        requiredCnt = len(t)

        # 里面放着滑动窗口 还需要多少字母(种类)
        required = Counter(t)

        while right < len(s):
            # 当s[r]是我们需要的字母
            if s[right] in required and required[s[right]] > 0:
                requiredCnt -= 1
            required[s[right]] -= 1

            #  当我们已经找完所需要的字母，记录长度，并试图缩小范围
            while requiredCnt == 0:

                # 记录长度
                if right - left + 1 < length:
                    start = left
                    length = right - left + 1

                # 缩小范围，移动滑动窗口的左边界
                if s[left] in required:
                    required[s[left]] += 1
                    if required[s[left]] > 0:
                        requiredCnt += 1

                # 假如缩小范围失败，退出循环
                # 假如缩小范围成功，进入下一轮循环
                left += 1

            # 移动右指针
            right += 1

        return "" if length == len(s) + 1 else s[start:start + length]

"""
https://algocasts.io/episodes/6emEOnpV
 Time: O(n), Space: O(n)
 写法：双指针 + hashmap
答案：
algocast用了一个256位的hashmap来创造map,但是我们可以用python 的collection.Counter 来产生一样的效果，就是有些代码需要改一下
"""









