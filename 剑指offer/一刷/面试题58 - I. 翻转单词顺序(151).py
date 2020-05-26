""""
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。

示例 1：
输入: "the sky is blue"
输出: "blue is sky the"

示例 2：
输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

示例 3：
输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s and len(s) == 0:
            return ""

        s = list(s)

        # l代表的是新字符串的指针， r代表的是旧字符串的指针
        l = 0
        r = 0
        end = len(s) - 1

        # end 的作用是指向最后一个字符， 例如 "  abc   ", 这个end 指向c
        while 0 <= end and s[end] == " ":
            end -= 1

        # 我们规定了遍历最远不超过右边
        while r <= end:
            # 记录单词被移动完后，最开始的位置
            start = l

            # 我们把r从左到右，有单词的第一个字符 例如 "  abc   ", 这个r 指向a
            while r <= end and s[r] == " ":
                r += 1

            # 我们要让r刚好遍历完一个单词，那么遍历结束的标志就是空格键， 例如 "abc de"中间的空格
            while r <= end and s[r] != " ":
                # 然后把r上的元素， 往l上填
                s[l] = s[r]
                r += 1
                l += 1

            # 因为其实最后一次循环，l就已经到一个单词结束的最后index,但是还+1了
            # 所以这里reverse 是，[start, l-1]
            self.reverse(s, start, l - 1)

            if r <= end:
                # 在我们刚放置好的单词后面插入一个空格
                s[l] = " "
                # 然后把l放置在下一个准备放单词的位置
                l += 1

        # 我们再把整个新字符串翻转一便
        self.reverse(s, 0, l - 1)

        return "".join(s[:l])

    def reverse(self, s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1