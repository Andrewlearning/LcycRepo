"""
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。
例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。
示例 1：

输入：["bella","label","roller"]
输出：["e","l","l"]

我们要做的是，把所有单词里都存在的字母都找出来放进列表里
"""


class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        res = []

        if not A:
            return res

        chars = set(A[0])
        for char in chars:

            # 关键一步，找出每个 char 在每个单词里的出现次数， 然后把最小的那个筛选出来
            minimum = min(word.count(char) for word in A)

            # 然后把结果加进res里
            res += [char] * minimum

        return res


"""
本题可以和350放在一起看
"""