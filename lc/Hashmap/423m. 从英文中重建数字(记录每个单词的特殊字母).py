"""
给定一个非空字符串，其中包含字母顺序打乱的英文单词表示的数字0-9。按升序输出原始的数字。

注意:

输入只包含小写英文字母。
输入保证合法并可以转换为原始的数字，这意味着像 "abc" 或 "zerone" 的输入是不允许的。
输入字符串的长度小于 50,000。
示例 1:

输入: "owoztneoer"

输出: "012" (zeroonetwo)
示例 2:

输入: "fviefuro"

输出: "45" (fourfive)
"""
import collections
class Solution(object):
    def originalDigits(self, s):
        """
        “z” 只在 “zero” 中出现。同时带走o
        “g” 只在 “eight” 中出现, 同时把h给带走了
        “h” 在剩下的单词中只有"three"有
        “w” 只在 “two” 中出现。同时把o带走
        “x” 只在 “six” 中出现
        “u” 只在 “four” 中出现。同时把f，o带走
        "f" 在剩下的单词中只有"five"有
        "o" 在剩下的单词里只有"one"有
        “s" 在剩下的单词里只有"seven"有
        "n" 在剩下的单词里只有"nine“有
        """

        name = ["zero", "one", "two", "three", "four", "five",
                "six", "seven", "eight", "nine"]

        # 我们做单词检测的顺序
        order = [0, 8, 3, 2, 6, 4, 5, 1, 7, 9]

        # 得到输入每个字母的出现次数
        hashmap = collections.Counter(s)

        res = []

        for num in order:
            # 开始对当前单词来进行筛选
            while True:
                # 判断当前单词在s里存不存在
                flag = True
                word = name[num]
                for char in word:
                    # 假如当前字母在hashmap里，且还有剩余
                    if char in hashmap and hashmap[char] > 0:
                        continue
                    # 不存在
                    else:
                        flag = False

                # 假如单词存在，我们要记录它
                if flag:
                    # 储存结果
                    res.append(str(num))
                    # 去除当前单词在hashmap里出现的次数
                    for char in word:
                        hashmap[char] -= 1
                # 不存在的话则结束死循环
                else:
                    break

        res.sort()
        return "".join(res)

# https://www.acwing.com/video/1828/
