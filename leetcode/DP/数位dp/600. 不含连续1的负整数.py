"""
给定一个正整数 n，找出小于或等于 n 的非负整数中，其二进制表示不包含 连续的1 的个数。

示例 1:

输入: 5
输出: 5
解释:
下面是带有相应二进制表示的非负整数<= 5：
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
其中，只有整数3违反规则（有两个连续的1），其他5个满足规则。
"""
class Solution(object):
    def findIntegers(self, n):
        """
        :type num: int
        :rtype: int
        """
        # 把num每一位都装进nums里去
        nums = []
        while n:
            nums.append(n % 2)
            n //= 2

        # dp[第几位数][0或1] 的二进制位上不含两个连续1的方案数
        dp = [[0] * 2 for _ in range(len(nums) + 1)]

        # 假如只有二进制只有一位数的话，那么填0，1都是合法的
        dp[1][0] = dp[1][1] = 1

        # 我们只用不构成连续1就行，所以dp[i][0] 的下一位是0或1都可以
        # 但是dp[i][1]不行，因为不能有连续的1，所以下一位只能是dp[i][0]
        for i in range(2, len(nums) + 1):
            dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
            dp[i][1] = dp[i - 1][0]

        res = 0
        # 上一位存的是什么数，用来判断有无出现两个1
        last = 0
        for i in range(len(nums), 0, -1):
            # dp[i]位等于 nums[i-1]位
            # 当前位的数
            x = nums[i - 1]

            # x == 1,说明存在一个比当前小的可能性, 那就是当前位取0
            if x == 1:
                res += dp[i][0]
                # 假如当前位时1，且上一位也是1，说明在往下的数，是存在11这样的序列，
                # 不合法，于是把前面合法结果返回
                if last == 1:
                    return res

            last = x

        # 假如所有位遍历完都是合法的，那可以加上n本身
        return res + 1

# https://www.acwing.com/video/2095/