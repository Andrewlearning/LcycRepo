class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # 单调栈在这里纯粹通过"筛选"的元素, 记录的结果即为我们最终想要的答案
        # 从小到大排列
        stack = []

        for i in range(len(num)):
            x = num[i]
            # 假如我们还有删数字的份额
            # 且栈里有元素，我们才能pop
            # 且 num[i-1] > num[i], 说明把num[i-1]删了，总体数字才能变小
            while k and stack and int(x) < int(stack[-1]):
                stack.pop()
                k -= 1

            stack.append(x)

        # 因为进过上面的处理，我们的序列应该是递增的，所以我们把stack后续删掉会更好
        while k:
            stack.pop()
            k -= 1

        if not stack:
            return "0"

        # 解决 "0200"的情况，因为要输出"200"
        return str(int("".join(stack)))

"""
贪心的分析：https://www.acwing.com/video/1798/
------ [i-1] [i]
三种情况
1. i-1 > i, 那么我们肯定希望在前面的数小一点啊，所以要删[i-1]，同时删完[i-1]后会继续看[i-2]和[i], 要是[i-2]还 > i, 那么[i-2]会继续被删，直到前面 < [i]为止
2. i-1 < i, 前面都比后面小了，假如删了之后第[i-1]位数会变大，所以不删
3. i-1 = i, 说明删不删都可以，跳过，把删的机会留给后面

可以和316一起看
"""