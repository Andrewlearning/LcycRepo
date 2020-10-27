class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []

        for char in num:
            # 假如我们还有删数字的份额
            # 且栈里有元素，我们才能pop
            # 且 num[i-1] > num[i], 说明把num[i-1]删了，数字能变小
            while k and stack and int(char) < int(stack[-1]):
                stack.pop()
                k -= 1

            stack.append(char)

        # 因为进过上面的处理，我们的序列应该是递增的，所以我们把后续删掉会更好
        while k:
            stack.pop()
            k -= 1

        if not stack:
            return "0"

        # 解决 "0200"的情况，因为要输出"200"
        return str(int("".join(stack)))

"""
https://blog.csdn.net/fuxuemingzhu/article/details/81034522
贪心的分析：https://www.acwing.com/video/1798/
------(i-1) (i)
三种情况
1. i-1 > i, 那么我们肯定希望在前面的数小一点啊，所以要删i-1
2. i-1 < i, 前面都比后面小了，假如删了之后数会变大，所以不删
3. i-1 = i, 说明删不删都可以，跳过,那选择的机会留给后面
"""