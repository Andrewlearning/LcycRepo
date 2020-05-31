
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 我们让l 指向的是，滑动窗口左边界的左边，r指向的是滑动窗口的右边界(l,r]
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
https://www.youtube.com/watch?v=COVvQ9I7XyI
答案：

2.我们一次遍历完整个字符串

    如果 s[i] 在之前出现过，**同时hashmap[s[i]] > start
    我们更新start,说明(start old, new start - 1]这一串都不要了
    要重新统计[new start,...]
    同时更新hashmap[s[i]]的value
    
    如果s[i] 没在之前出现过，**或者 hashmap[s[i]] < start
    说明这个元素我们愿意把它统计到最长子串中
    例如："tmmzuxt"
    
    我们愿意把最后一个t加入到我们的最长字串当中，因为第一个t我们早已不在字串中了（index<start)
    所以这个最后这个t我们要把它加进去
    
"""