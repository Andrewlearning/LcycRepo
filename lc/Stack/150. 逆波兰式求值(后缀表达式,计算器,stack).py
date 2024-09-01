"""
根据 逆波兰表示法，求表达式的值。
有效的运算符包括+,-,*,/。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

说明：
整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。


示例1：

输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: 该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for t in tokens:
            if t in "+-*/":
                y = nums.pop()
                x = nums.pop()
                if t == "+":
                    nums.append(x + y)
                elif t == "-":
                    nums.append(x - y)
                elif t == "*":
                    nums.append(x * y)
                else:
                    # 在python里面 遇到 -1/22 这种情况，会 = -0.004xxxx
                    # 但是这里要求的是 -1/22 = 0, 所以我们用 int(float(devidend) / devisor) 来使-0.0004x向下取整变成0
                    nums.append(int(float(x) / y))
            else:
                nums.append(int(t))

        return nums[-1]


"""
https://www.acwing.com/video/1522/
这就是逆波兰表达式的做法:
遇到一个数，把它加到栈顶
遇到一个符号，就把栈顶元素取出来处理一下


注意，在python里面 遇到 -1/22 这种情况，会 = -0.004xxxx
    但是这里要求的是 -1/22 = 0, 所以我们用 int(float(devidend)) / devisor 来使-0.0004x向下取整变成0
    int()总是向下取整
    
什么是逆波兰表达式
平时我们习惯将表达式写成 (1 + 2) * (3 + 4)，加减乘除等运算符写在中间，因此称呼为中缀表达式
而波兰表达式的写法为 (* (+ 1 2) (+ 3 4))，将运算符写在前面，因而也称为前缀表达式
逆波兰表达式的写法为 ((1 2 +) (3 4 +) *)，将运算符写在后面，因而也称为后缀表达式
    逆波兰表达式去掉圆括号，变成 1 2 + 3 4 + * 也是无歧义并可以计算的
链接：https://www.zhihu.com/question/41103160/answer/452481026
"""