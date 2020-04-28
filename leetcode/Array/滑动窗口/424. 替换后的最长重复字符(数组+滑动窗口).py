class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0

        # 我们用一个数组来记录26个字母 在滑动窗口内出现的次数
        hashmap = [0 for i in range(26)]
        l = 0
        n = len(s)
        charMax = 0

        # 在for循环中，我们不断移动滑动窗口的右边界
        for r in range(n):
            # 我们先把char 转化成0-26的其中一个下标
            index = ord(s[r]) - ord("A")

            # 然后我们把对应下标的个数+1， 表面
            hashmap[index] += 1

            # 我们每一次循环都要找出滑动窗口内出现次数最多的char
            # 这样替换的时候我们就可以筛选出   用出现次数最多的+最多可替换的数量是多少
            charMax = max(charMax, hashmap[index])

            # 假如说滑动窗口长度 > 替换后的最长重复字符，
            # 那么说明在当前窗口范围内的字母串，不可能产生新的最大 替换字符串
            # 那么我们要调整滑动窗口的位置，使它尝试下一个位置
            if r - l + 1 > charMax + k:
                hashmap[ord(s[l]) - ord("A")] -= 1
                l += 1

        return n - l

"""
Time: O(n)
Space: O(n)
https://leetcode-cn.com/problems/longest-repeating-character-replacement/solution/tong-guo-ci-ti-liao-jie-yi-xia-shi-yao-shi-hua-don/
那么这个题的关键点就是我们如何判断一个字符串改变K个字符，能够变成一个连续串

如果当前字符串中的出现次数最多的字母个数+K大于串长度，那么这个串就是满足条件的

我们维护一个数组int[26]来存储当前窗口中各个字母的出现次数，left表示窗口的左边界，right表示窗口右边界

窗口扩张：left不变，right++
窗口滑动：left++, right++
charMax保存滑动窗口内相同字母出现次数的历史最大值，通过判断窗口宽度(right - left + 1)是否大于charMax + K来决定窗口是否做滑动，否则窗口就扩张

"""