"""
判断是是否为回文数字，12321 可以 ， -121 ！= 121-不可以
0 可以
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        origin = x
        reverse = 0

        while x:
            # 每次取下x的最后一位元素 x=121 -> last=1
            last = x % 10
            # 并把最后一位元素添加到reverse后面，reverse = 0 * 10 + 1
            reverse = reverse * 10 + last

            # x = 121//10 = 12
            x //= 10

        return reverse == origin

"""
这题其实跟7,reverse integer很像
// Time: O(m), Space: O(1)
https://algocasts.io/episodes/zbmKMpZq
答案：
1.我们已知负数是一定不行的，所以x<0,return false
2.我们用res来计算x的相反数字
3.res*10等于把原来有的数进位，9 -> 90, + temp%10,把temp最末尾一位加到res
4.return时对比两者是否相同
"""