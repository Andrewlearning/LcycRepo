"""
神奇的字符串S只包含 '1' 和 '2'，并遵守以下规则：

字符串 S 是神奇的，因为串联字符 '1' 和 '2' 的连续出现次数会生成字符串 S 本身。

字符串S的前几个元素如下：S = “1221121221221121122 ......”

如果我们将S 中连续的 1 和 2 进行分组，它将变成：

1 22 11 2 1 22 1 22 11 2 11 22 ......

并且每个组中 '1' 或 '2' 的出现次数分别是：
1 22 11 2 1 22 1 22 11 2 11 22 ......
1 2  2  1 1 2  1 2  2  1 2 2 ......

"""

class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """

        s = "122"
        res = 0
        # 122后面下一个数字是1
        k = 1

        # i表示s字符串第i位应该是什么数
        for i in range(2, n):
            # 下一个数字(k)应该出现几次
            m = int(s[i])

            # 加上出现几次
            for j in range(m):
                s += str(k)

            # 因为是1，2交替，用这个方式进行转换
            k = 3 - k

        # 看s里面有多少个1
        for i in range(n):
            if s[i] == '1':
                res += 1
        return res

# https://www.acwing.com/activity/content/code/content/606125/