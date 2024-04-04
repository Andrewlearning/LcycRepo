"""
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为 1，那么这个数就是快乐数。

如果 n 是快乐数就返回 True ；不是，则返回 False 。



示例：

输入：19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = []

        while n != 1:
            cur = self.getDigit(n)

            # 当运算结果为1时，为True
            if cur == 1:
                return True
            # 假如运算结果重复出现时，说明进入死循环，无法得到1，返回false
            if cur in visited:
                return False

            visited.append(cur)
            n = cur
        return True

    def getDigit(self, n):
        res = 0
        while n > 0:
            cur = n % 10
            res += cur ** 2
            n = n // 10
        return res

"""
Time: O(1), Space: O(1)
https://algocasts.io/episodes/6emEKnpV
答案：
1.假如我们一直求 位数的平方和，我们知道，只有找到1的时候才能破除循环，但是找不到1的时候，什么情况才是终止条件呢？
2. 答案是，我们用一个set来存放位数的平方和，假如说一直都到不了1的话，总有一天能刷出set(）有的元素
   到那个时候就return False

"""