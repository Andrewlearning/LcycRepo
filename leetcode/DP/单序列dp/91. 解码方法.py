"""
一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：
"AAJF" ，将消息分组为 (1 1 10 6)
"KJF" ，将消息分组为 (11 10 6)

注意，消息不能分组为  (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。

给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。

题目数据保证答案肯定是一个 32 位 的整数。
"""

class Solution(object):
    # // Time: O(n), Space: O(n)
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s and len(s) == 0:
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        # 给第一个两位数做准备
        dp[0] = 1

        # 假如第一个元素是0的话，那么dp[1] = 0
        if s[0] != "0":
            dp[1] = 1
        else:
            dp[1] = 0

        for i in range(2, len(dp)):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            if self.twodigitvalid(s[i - 2], s[i - 1]):
                dp[i] += dp[i - 2]
        return dp[n]

    # // Time: O(n), Space: O(1)
    def numDecodings_yaso(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0: return 0

        prev2 = 1
        prev1 = 1 if s[0] != "0" else 0

        for i in range(2, len(s) + 1):
            cur = 0
            if s[i - 1] != "0": cur += prev1
            if self.twodigitvalid(s[i - 2], s[i - 1]):
                cur += prev2
            prev1, prev2 = cur, prev1
        return prev1

    def twodigitvalid(self, a, b):
        if a == "1" and b <= "9" or a == "2" and b <= "6":
            return True
        return False

"""
https://discuss.algocasts.io/t/topic/104/2
答案：
1.我们这样看 例如 "1245", dp[1] = "1"
                       dp[2] = "1",""
                       dp[3] = "12","1"
                       dp[4] = "124","12" = dp[3]+dp[2]
   在dp[0],dp[1]中，我们无法拿掉一个或者两个字符，所以dp[0]的大小是， dp[1]的大小取决于第一位数是不是1-9
   而在dp[2]以及往后，字符串长度>=2,于是我们可以拿掉字符串后面的一位或者两位
   因为"124"的编码可能性等于，"4"(1) * "12"(12的所有可能性) = "12"（12的所有可能性）
                            "24"(1) * "1"(1的所有可能性) = "1"（1的所有可能性）
                            
   有点像跳楼梯的那个题，因为从第三个楼梯，无论如何都要往下跳一步或者两步，所以第三格往下跳的可能性
   等于第三格往下跳（1） * 第二格往下跳（dp[i-1]） = dp[i-1]
   
   同样的，由于递推式子只有简单的dp[i] , dp[i-1], dp[i-2]，所以我们可以用三个常量来代替它，从而降低
   空间复杂度
"""