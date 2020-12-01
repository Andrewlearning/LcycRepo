"""
把字符串 s 看作是“abcdefghijklmnopqrstuvwxyz”的无限环绕字符串，
所以s 看起来是这样的："...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
现在我们有了另一个字符串 p 。你需要的是找出 s 中有多少个唯一的 p 的非空子串，尤其是当你的输入是字符串 p ，你需要输出字符串 s 中 p 的不同的非空子串的数目。 
注意: p仅由小写的英文字母组成，p 的大小可能超过 10000。
示例1:
输入: "a"
输出: 1
解释: 字符串 S 中只有一个"a"子字符。

示例 2:
输入: "cac"
输出: 2
解释: 字符串 S 中的字符串“cac”只有两个子串“a”、“c”。.

示例 3:
输入: "zab"
输出: 6
解释: 在字符串 S 中有六个子串“z”、“a”、“b”、“za”、“ab”、“zab”。.
"""
import collections
class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """

        hashmap = collections.defaultdict(int)

        # 字符串第一个字符，肯定是1的
        # key 子字符串最后一个字母
        # value 字母结尾形成的最长连续的字符串长度
        hashmap[p[0]] = 1

        maxLen = 1

        # 跳过第一个字符，开始遍历
        for i in range(1, len(p)):
            pre = p[i-1]
            cur = p[i]

            # 说明当前字符串满足 zabcd..这样的顺序
            # 所以可以叠加这个连续字符串所能得到的所有子串个数
            # 例如 abc -> a, ab, abc
            #     abcd -> a, ab, abc, abcd
            # 然后这个连续字符串有多长，其实也代表这个串能构成多少个唯一字符串
            if (ord(cur) - ord(pre)) % 26 == 1:
                maxLen += 1
            else:
                maxLen = 1

            # 每次更新这个字母结尾形成的最长连续的字符串长度
            hashmap[cur] = max(maxLen, hashmap[cur])

        return sum(hashmap.values())

        # https://leetcode-cn.com/problems/unique-substrings-in-wraparound-string/solution/zhao-zui-chang-lian-xu-zi-fu-chuan-chang-du-by-pow/