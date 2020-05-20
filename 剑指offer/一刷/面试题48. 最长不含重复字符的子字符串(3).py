class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # 我们让l 指向的是，滑动窗口左边界的左边，r指向的是滑动窗口的右边界
        l = -1
        r = 0

        hashmap = {}
        length = len(s)
        res = 0

        while r < length:
            # 当s[r]这个元素已经在hashmap中，且s[r]这个元素是在滑动窗口中
            # 因为hashmap的元素，不会因为不在滑动窗口内，就删除
            # 所以得到s[r] 对应的index，有可能是不在滑动窗口内的
            if s[r] in hashmap and hashmap[s[r]] > l:

                # 更新滑动窗口左边界，且s[r]这个元素已经不在窗口内了
                l = hashmap[s[r]]
                # 把这个元素的新下标放进hashmap
                hashmap[s[r]] = r

            # if s[r] 不在 hashmap
            else:
                hashmap[s[r]] = r
                res = max(res, r - l)

            r += 1

        return res
"""
对应lc第三题
"""