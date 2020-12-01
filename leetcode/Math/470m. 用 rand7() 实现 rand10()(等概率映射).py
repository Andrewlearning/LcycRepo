"""
Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10.

Do NOT use system's Math.random().
Example 1:
Input: 1
Output: [7]
Example 2:
Input: 2
Output: [8,4]
"""
# The rand7() API is already defined for you.
def rand7():
    pass
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        rand40 = 41

        while rand40 > 40:
            # rand7() - 1 -> [0~6]
            # (rand7() - 1) * 7 -> [0, 7, 14, 21, 28, 35]
            # [0, 7, 14, 21, 28, 35]是随机出现
            # [1,2,3,4,5,6,7] 也是随机出现
            # 他们两相加会出现42种唯一组合，且都每种组合都代表【1-42】的其中一个数，所以概率相等
            # 大于40的我们直接过滤掉
            rand40 = (rand7() - 1) * 7 + rand7()
        return rand40 % 10 + 1



"""
https://algocasts.io/episodes/JNmDVZpO
解释
这个问题有两个形式：
rand 大数生成小数
rand 小数生成大数

第一种
譬如 rand10得到rand7
思路很简单，如果得到8-10，就继续调用，直到处于1-7为止
但是遇到 rand50得到rand7 呢？
做个取余就好1-49 映射到 1-7很容易，50就继续循环调用
你会发现这个题目的核心就是 等概率映射，映射不到的就继续调用

第二种
小数生成大数，核心也是一样，等概率映射
我们自然而然就会想到，乘以一个数试试
譬如 rand7得到rand10
把7乘以2,得到14，不就大于10了吗？Ok搞定！！
等等，你会发现，1-14这个范围是有问题的，1根本不会出现！
而像 5，有多重出现方式 1+4，2+3
也就是说，我们的数没有等概率出现。
我们最好是让每个数，只能有且一种组合方式出现
rand7 + (rand7 - 1) * 7
1-10，11-20，21-30，31-40
都是等概率出现的，每个数只能有且一种组合方式出现

你会发现，这就是一个7进制！！
进一个 1就对应一个新数，因为这个7位数，1-7就代表一个数，进一位 1 (也就是7) ，就是对于另外一个数
链接：https://leetcode-cn.com/problems/implement-rand10-using-rand7/solution/xiang-xi-fen-xi-fei-chang-jing-dian-de-ti-mu-deng-/

"""