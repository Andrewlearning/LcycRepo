"""
Given an input string, reverse the string word by word.
（按照单词来进行反转，但是要注意忽略掉前面的空格）
Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
"""


class Solution(object):

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s and len(s) == 0:
            return s

        string = list(s)

        # l放的是符合规范的单词和空格
        l = 0
        # r是探路者
        r = 0

        # end是去除末尾空格后的最后一位
        end = len(string) - 1

        # 去除字符串末尾的空格
        while end >= 0 and string[end] == " ":
            end -= 1

        # 全是空格的情况
        if end == -1:
            return ""

        while r <= end:
            start = l

            # 让r走到单词的开头
            while r <= end and string[r] == " ":
                r += 1

            # r在单词上走
            while r <= end and string[r] != " ":
                # 把r的元素，填到l的位置上去，这样能把字符串首部的空格去掉
                string[l] = string[r]
                l += 1
                r += 1

            # 把一个单词填完以后，我们把这个单词反转
            self.reverse(start, l - 1, string)

            # 假如说r还没走到尽头，且一个单词已经填完到l的位置上了，那么给l的位置上加一个空格
            if r <= end:
                string[l] = " "
                l += 1

        # 最后，我们把所有单词都反转了，并且空格只有一个，然后我们把整体都反转，得到答案
        self.reverse(0, l - 1, string)

        return "".join(string[:l])

    def reverse(self, start, end, string):
        while start < end:
            string[start], string[end] = string[end], string[start]
            start += 1
            end -= 1

"""
https://algocasts.io/episodes/BPp63kWr
// Time: O(n), Space: O(n)
答案：
1.首先处理corner case
2.创建一个string的list, p代表新string的指针，q代表旧string的指针
他们两个都在string上遍历，替换是inplace的
3.先把string后面的空格给去掉，用end --
4.然后就可以开始while r <= end: 开始把开头的空格去掉，用q++
5.当q到达正主的时候（单词），开始和p进行inplace赋值
6.附值在q遇到空格是停止，那是单词中间的间隙，这时候要开始reverse新附值的单词了【start,l-1]
7.把单词反转过后，加上空格，重复5-7的过程
8.所有单词反转过之后，最后整体再反转一遍，得到结果

例子 "apple care"
     elppa  erac(先把每个单词反转一遍)
     care apple（最后整体反转一遍）得到结果

"""










