"""
给定一个字符串 s ，找出 至多 包含 k 个不同字符的最长子串 T。

示例 1:

输入: s = "eceba", k = 2
输出: 3
解释: 则 T 为 "ece"，所以长度为 3。

"""

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        n = len(s)
        if n * k == 0:
            return 0

        hashmap = {}

        l = 0
        r = 0
        res = 0

        while r < n:
            # 假如hashmap里有这个元素的话，那么更新value
            # 假如hashmap里有这个元素的话，那么新增一对key-value
            hashmap[s[r]] = r
            r += 1

            # 说明字典里面已经有超过K个不同的字母了， 那么我们要对滑动窗口进行处理
            if len(hashmap) > k:

                # 说明滑动窗口里已经有超过两个不同的字母了， 那么我们要对滑动窗口进行处理
                leftmost = len(s)
                for index in hashmap.values():
                    if index < leftmost:
                        leftmost = index

                # 找到滑动窗口最左边的元素，然后把该元素从字典里面去除
                del hashmap[s[leftmost]]

                # 删掉最左边的不重复数组后，调整滑动窗口的左位置
                l = leftmost + 1

            res = max(res, r - l)
        return res

"""
https://leetcode-cn.com/problems/longest-substring-with-at-most-k-distinct-characters/solution/zhi-shao-bao-han-k-ge-bu-tong-zi-fu-de-zui-chang-z/
时间复杂度: O(Kn), 因为查找字典可能里面有k个tuple
空间复杂度：O(k), 因为hashmap里最多有k个tuple
解答过程基本上和159一摸一样
只不过在本题里面，把两个不同字符改成了k个不同字符
还有边界情况处理有点不一样
"""








