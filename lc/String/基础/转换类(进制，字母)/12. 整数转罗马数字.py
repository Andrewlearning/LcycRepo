"""
罗马数字包含以下七种字符：I，V，X，L，C，D和M。
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

例如， 罗马数字 2 写做II，即为两个并列的 1。12 写做XII，即为X+II。 27 写做XXVII, 即为XX+V+II。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做IIII，而是IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
同样地，数字 9 表示为IX。这个特殊的规则只适用于以下六种情况：

I可以放在V(5) 和X(10) 的左边，来表示 4 和 9。
X可以放在L(50) 和C(100) 的左边，来表示 40 和90。
C可以放在D(500) 和M(1000) 的左边，来表示400 和900。
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # 在3999的范围以内，我们列举了所有可能出现的面值
        # 我们要做的是，从大到小的遍历他们，因为罗马数字的规律是，大的数字总是放在左边，小的数总是放在右边
        # 例如 1101 = 1000(M) + 100(C) + 1(I) -> MCI
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        sbs = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        n = len(nums)
        res = []

        for i in range(len(values)):
            # 注意：这里是等于号，表示尽量使用大的"面值"

        while num > 0:
            for i in range(n):
                # 从大往小遍历，当发现可以相减的，记录
                if nums[i] <= num:
                    num -= nums[i]
                    res.append(sbs[i])
                    # 减完一次重新开始，要不然会把较小的数放在左边
                    break

        return "".join(res)

"""
https://leetcode-cn.com/problems/integer-to-roman/solution/tan-xin-suan-fa-by-liweiwei1419/
解题思想
本题“整数转罗马数字”也有类似的思想：在表示一个较大整数的时候，“罗马数字”的设计者不会让你都用 11 加起来
我们总是希望写出来的“罗马数字”的个数越少越好，以方便表示，并且这种表示方式还应该是唯一的。
"""