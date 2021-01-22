"""
单调栈问题解决的是：
一个队列，求每一个数，左边(右边)离它最近的，且比它小(大)的数，在什么地方

题目：
找到每一个数在左边离它最近，且比它小，返回这个数，不然返回-1
题目：3，4，2，7，5
答案：-1,3,-1,2,2
"""

if __name__ == "__main__":

    n = int(input())

    nums = list(map(int, input().split()))

    # 储存着一个在num之前的，有单调性的数组
    stack = []
    res = []

    for num in nums:
        # 在这里，我们要构造单调性，我们要保证这个单调栈，一定是从小到大
        # 或是从大到小
        while len(stack) and stack[-1] >= num:
            stack.pop()

        # 假如单调栈还存在比当前num大的数，那么说明栈顶元素就是在当前元素
        # 小，且最靠近当前元素的一个数
        if len(stack) > 0:
            res.append(stack[-1])
        else:
            res.append(-1)

        stack.append(num)

    print(" ".join(map(str, res)))

# https://www.acwing.com/video/258/