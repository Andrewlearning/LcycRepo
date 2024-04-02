"""
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s:
            return ""

        res = [""] * numRows
        # i用来记录使用了多少个字母
        i = 0

        while i < len(s):

            """
            from up to down
            j表示y轴，用来记录字母在竖直方向上要往哪一行进行拼接
            j的移动范围是[0 ~ numRows - 1]
            [
                "P",
                "A",
                "Y",
                "P"
            ]
            """
            j = 0
            while i < len(s) and j < numRows:
                res[j] += s[i]
                i += 1
                j += 1

            """
            from down to up
            往上加的时候，注意最后一行，和第一行是到不了的
            所以从倒数第二行(numsRow-2) 开始到 第二行(j = 1)结束
            [
                "P",
                "AY",
                "YA",
                "P"
            ]
            """
            j = numRows - 2
            while i < len(s) and j > 0:
                res[j] += s[i]
                i += 1
                j -= 1

        return "".join(res)

if __name__ == '__main__':
    s = Solution()
    print(s.convert("PAYPALISHIRING", 4))

"""
https://www.youtube.com/watch?v=8zXTAn7i5rU
这题其实找到规律了就很好写
创建一个多维列表
然后按照列表的
从上往下，再从下往上那样写，最后把每一行给拼起来

P     I    N
A   L S  I G
Y A   H R
P     I
"""
