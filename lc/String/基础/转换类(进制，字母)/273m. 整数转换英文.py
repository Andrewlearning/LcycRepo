"""
将非负整数转换为其对应的英文表示。可以保证给定输入小于 231 - 1 。

示例 1:

输入: 123
输出: "One Hundred Twenty Three"
示例 2:

输入: 12345
输出: "Twelve Thousand Three Hundred Forty Five"
示例 3:

输入: 1234567
输出: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
示例 4:

输入: 1234567891
输出: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        def helper(num):
            # index0 对应 one, 所以to19[num - 1]
            if num < 20:
                # 这里用来返回对应的数字，同时处理
                return to19[num - 1:num]
            # 十位：index0 对应 twenty, 所以tens[num//10 -2]
            # 个位：helper(num%10), 交给专门的个位处理
            if num < 100:
                return [tens[num // 10 - 2]] + helper(num % 10)
            # 百位: 把最高位处理掉，换成to19
            # 剩下的按照十位处理
            if num < 1000:
                return [to19[num // 100 - 1]] + ["Hundred"] + helper(num % 100)
            # 这里刚好是三者的规律 Thousand * 1000 = Million * 1000 = Billion
            for p, w in enumerate(["Thousand", "Million", "Billion"], 1):
                # 首先我们判断num是处于哪个档次
                if num < 1000 ** (p + 1):
                    # 然后把他按照他的档位，进行最高位处理
                    # 剩下的则%1000交给 num<1000处理
                    return helper(num // 1000 ** p) + [w] + helper(num % 1000 ** p)

        # 最后把一个个[]拼在一起
        return " ".join(helper(num)) or "Zero"

"""
https://leetcode-cn.com/problems/integer-to-english-words/solution/zheng-shu-zhuan-huan-ying-wen-biao-shi-by-powcai/
"""