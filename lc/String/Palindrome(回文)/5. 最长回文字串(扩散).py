class Solution(object):
    def expend(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > len(self.res):
                self.res = s[l:r+1]
            l -= 1
            r += 1

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) == 0:
            return ""

        self.res = ""
        for i in range(len(s)):
            self.check(s, i, i)
            self.check(s, i, i+1)
        return self.res


"""
https://algocasts.io/episodes/VBpLqWD8
Time: O(n^2), Space: O(1)
答案：
1.本体的解体关键函数是 expend函数，他的作用是，给定两个index,会一直对比，看 nums[l] ==? nums[r]
 一直向外扩散

2.所以在主函数里面，我们定下了两个len,分别调用这个函数，之所以这样调用，是
  有可能出现 1 2 3 2 1 
  或者      1 1 2 2 3 3 这两种回文的情况

3. 精妙的在这里，我们要找出这个回文字串的起始 index
   start = i(当前index) - (字串长度 - 1) // 2
   
   例如： i = 2, 1 2 3 2 1 
         那么start = 2 - (5-1)//2 = 0 (正确）
         i = 2, 1 1 2 2 1 1 
         那么start = 2 - （6-1)//2 = 0(正确）

4.我们返回 s[start: start+maxLen]就好了 
"""
