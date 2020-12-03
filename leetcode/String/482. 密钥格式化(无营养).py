"""
有一个密钥字符串 S ，只包含字母，数字以及 '-'（破折号）。其中， N 个 '-' 将字符串分成了 N+1 组。
给你一个数字 K，请你重新格式化字符串，使每个分组恰好包含 K 个字符。特别地，第一个分组包含的字符个数必须小于等于 K，但至少要包含 1 个字符。两个分组之间需要用 '-'（破折号）隔开，并且将所有的小写字母转换为大写字母。
给定非空字符串 S 和数字 K，按照上面描述的规则进行格式化。


示例 1：

输入：S = "5F3Z-2e-9-w", K = 4
输出："5F3Z-2E9W"
解释：字符串 S 被分成了两个部分，每部分 4 个字符；
    注意，两个额外的破折号需要删掉。
"""


class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = ""
        for c in S:
            if c != '-':
                s += c.upper()

        res = ""
        # 第一部分的数不要求一定要等于k，所以我们把余数在第一部分处理掉
        for i in range(len(s) % K):
            res += s[i]

        # 后面的数就都要满足k各一组了
        start = len(s) % K
        for j in range(start, len(s), K):
            # 有可能出现s长度刚好是k的倍数这种情况，那么上面那个循环将不会执行
            # 所以我们不能在这种情况的开头加 -
            if res:
                res += '-'
            res += s[j:j + K]
        return res

# https://www.acwing.com/activity/content/code/content/597966/
