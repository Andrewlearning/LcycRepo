"""
Given a string containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

Input: "()[]{}"
Output: true

Input: "(]"
Output: false
就是判断左右两边的括号能不能合上
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check = ["()","{}","[]"]
        stack = []
        for char in s:

            if char in "({[":
                stack.append(char)

            else:
                if len(stack) == 0:
                    return False

                cur = stack.pop(-1) + char
                if cur not in check:
                    return False

        return len(stack) == 0


"""
这题利用stack来做

remark:
1.注意else这种情况，有可能输入的只是一个右字符串，那么pop的话会返回错误结果
所以建议在输入右字符串的时候，先检测一下stack的长度，如果长度为0,那么直接return false
"""