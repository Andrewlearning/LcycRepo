"""
Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

无限循环小数应该这样处理
Input: numerator = 2, denominator = 3
Output: "0.(6)"
"""

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        num = numerator
        den = denominator

        # 分母为0
        if not den:
            return

        # 分子为0
        if not num:
            return "0"

        res = []
        if (num < 0) ^ (den < 0):
            res.append("-")

        num, den = abs(num), abs(den)
        res.append(str(num//den))

        # 看是否存在余数
        rmd = num % den

        #如果没有余数,返回整数结果
        if not rmd:
            return "".join(res)

        #无返回的话说明有余数，且需要进入到小数位
        res.append(".")

        # 余数:余数之前在res从左往右数的第几位出现
        dic = {}

        # 假如说还存在余数，说明没除完，循环继续下去
        while rmd:
            # 假如余数出现之前出现过了，说明出现了循环小数，例如1.3333
            if rmd in dic:
                # 那么我们在res里加上，( 重复的余数 )
                res.insert(dic[rmd], "(")
                res.append(")")
                break

            # 记录当前余数，以及它出现的位置
            dic[rmd] = len(res)
            # 更新被除数
            div = rmd*10 // den
            # 更新余数
            rmd = rmd*10 % den

            res.append(str(div))
        return "".join(res)


"""
思路：https://www.youtube.com/watch?v=WJMrceU-ujs
答案：https://leetcode.com/problems/fraction-to-recurring-decimal/discuss/51187/Python-easy-to-understand-solution-with-comments.
答案：

"""