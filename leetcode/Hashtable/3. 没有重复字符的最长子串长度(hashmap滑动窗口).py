
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {}
        left = -1
        maxLen = 0

        for right in range(len(s)):
            # s[right] in hashmap
            # abca,left = -1 -> left = 1
            if s[right] in hashmap and hashmap[s[right]] > left:
                left = hashmap[s[right]]
                hashmap[s[right]] = right
            # s[right] not in hashmap
            else:
                hashmap[s[right]] = right

            if right - left > maxLen:
                maxLen = right - left

        return maxLen

"""
https://www.youtube.com/watch?v=COVvQ9I7XyI
答案：
hashmap里 key是 字母， value是字母所对应的index

1.强调一点，这里计算长度的方式是 right - left, 这种计算方式是计算（left,right]的长度
所以一开始left 是等于-1，因为这样才可以计算从[0,right]的长度

2.我们一次遍历完整个字符串
            
    abac
      right   
    如果 s[right] (a) 在之前出现过，同时hashmap[s[right]] > left,这说明了在当前的(left,right]，有两个s[right]
    所以我们要更新left, 去创造一个不重复包括s[right]的新的(left,right]
    所以我们要更新left,left = hashmap[s[right]](第一个出现的s[right]的index)
    这表面我们从第一个a后面的字符开始计算
    同时更新hashmap[s[right]]的value，就是a的新index
    
    
    如果s[right]没在之前出现过，或者 hashmap[s[right]] < left,这说明在当前的(left,right)，还不存在当前元素
    说明这个元素我们要把把它统计到最长子串中
    例如："tmmzuxt"
    
    我们愿意把最后一个t加入到我们的最长字串当中，因为第一个t我们早已不在字串中了（index<left)
    所以这个最后这个t我们要把它加进去

"""