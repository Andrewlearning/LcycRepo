"""
格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。即使有多个不同答案，你也只需要返回其中一种。
格雷编码序列必须以 0 开头。

示例 1:

输入: 2
输出: [0,1,3,2]
解释:
00 - 0
01 - 1
11 - 3
10 - 2

对于给定的 n，其格雷编码序列并不唯一。
例如，[0,2,3,1] 也是一个有效的格雷编码序列。
"""
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # res记录的是上一轮的所有结果，是可以直接平移到下一轮
        res = [0]

        # head表示的是，如果有下一轮的话，新增的结果
        head = 1

        for i in range(n):
            # 之所以要倒序，是要满足各类编码 「两个连续的数值仅有一个位数的差异」 的规律
            for j in range(len(res) - 1, -1, -1):
                res.append(head + res[j])

            # 当前位加完了，head要继续移动到下一位
            head <<= 1
        return res

# 链接：https://leetcode-cn.com/problems/gray-code/solution/gray-code-jing-xiang-fan-she-fa-by-jyd/
