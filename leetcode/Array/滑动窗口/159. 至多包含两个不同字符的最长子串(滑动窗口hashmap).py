class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0

        # 用来记载滑动窗口里有多少个不同的元素
        # key: char, value:index
        hashmap = {}

        l = 0
        r = 0
        res = 0

        while r < len(s):
            # 假如hashmap里有这个元素的话，那么更新value
            # 假如hashmap里有这个元素的话，那么新增一对key-value
            hashmap[s[r]] = r
            r += 1

            # 说明滑动窗口里已经有超过两个不同的字母了， 那么我们要对滑动窗口进行处理
            if len(hashmap) > 2:
                leftmost = len(s)
                # 说明滑动窗口里已经有超过两个不同的字母了， 那么我们要对滑动窗口进行处理
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
时间复杂度：On 空间复杂度 O(1),因为hashmap里不超过三个元素
https://www.youtube.com/watch?v=2vW_Q8ToSAU

"""