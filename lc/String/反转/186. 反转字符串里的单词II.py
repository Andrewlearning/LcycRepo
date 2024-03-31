"""
给定一个字符串，逐个翻转字符串中的每个单词。

示例：

输入: ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
输出: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
"""

class Solution(object):
    def reverseWords(self, char):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        start = end = 0

        while start < len(char):
            # 目的是让end 移动到单词的后一位
            while end < len(char) and char[end] != " ":
                end += 1

            # 因为end 在单词的后一位，所以index上要-1， 使得i,j分别指向单词头和单词尾
            self.swap(char, start, end - 1)
            start = end + 1
            end = start

        self.swap(char, 0, len(char)-1)

        return "".join(char)

    def swap(self, array, i, j):
        while i < j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

"""
先把每个单词反转一次，然后再对整个字符串反转一次
做法和557一样
"""