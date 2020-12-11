"""
你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。

你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。

 

示例 1：

输入：name = "alex", typed = "aaleex"
输出：true
解释：'alex' 中的 'a' 和 'e' 被长按。
"""


class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = 0
        j = 0

        while j < len(typed):
            # 作为 name 的一部分。此时会「匹配」name 中的一个字符
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            # 作为长按键入的一部分。此时它应当与前一个字符相同。
            elif j > 0 and typed[j - 1] == typed[j]:
                j += 1
            else:
                return False

        return i == len(name)

# https://leetcode-cn.com/problems/long-pressed-name/solution/chang-an-jian-ru-by-leetcode-solution/