class Solution:
    def Add(self, num1, num2):
        while num2 != 0:
            sum = num1 ^ num2
            carry = (num1 & num2) << 1
            num1 = sum
            num2 = carry

        return num1

if __name__ == "__main__":
    solution = Solution()
    solution.Add(4,4)


"""
# 链接：https://leetcode-cn.com/problems/sum-of-two-integers/solution/wei-yun-suan-xiang-jie-yi-ji-zai-python-zhong-xu-y/

位运算中的加法
我们先来观察下位运算中的两数加法，其实来来回回就只有下面这四种：
0 + 0 = 0
0 + 1 = 1
1 + 0 = 1
1 + 1 = 0（进位 1）
仔细一看，这可不就是相同位为 0，不同位为 1 的异或运算结果嘛~

异或和与运算操作
我们知道，在位运算操作中，异或的一个重要特性是无进位加法。我们来看一个例子：


a = 5 = 0101
b = 4 = 0100

a ^ b 如下：
0 1 0 1
0 1 0 0
-------
0 0 0 1

a ^ b 得到了一个无进位加法结果，如果要得到 a + b 的最终值，我们还要找到进位的数，把这二者相加。在位运算中，我们可以使用与操作获得进位：


a = 5 = 0101
b = 4 = 0100

a & b 如下：

0 1 0 1
0 1 0 0
-------
0 1 0 0

"""