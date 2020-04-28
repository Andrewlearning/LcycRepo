class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0

        hashmap = {}

        l = 0
        r = 0
        res = 0

        while r < len(s):
            hashmap[s[r]] = r
            r += 1

            # 说明字典里面已经有超过两个不同的字母了， 那么我们要对滑动窗口进行处理
            if len(hashmap) > 2:
                leftmost = len(s)
                for index in hashmap.values():
                    if index < leftmost:
                        leftmost = index

                # 找到滑动窗口最左边的元素，然后把该元素从字典里面去除
                del hashmap[s[leftmost]]

                # 调整滑动窗口的位置
                l = leftmost + 1

            res = max(res, r - l)
        return res

"""
时间复杂度：On 空间复杂度 O(1),因为hashmap里不超过三个元素
https://www.youtube.com/watch?v=2vW_Q8ToSAU

"""