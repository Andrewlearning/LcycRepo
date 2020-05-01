"""
有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。

现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束。
"""

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        res = bits.pop(-1)

        # 奇数情况 0 1110     假如说最后0前面有奇数个连续的1，那么最后一个必为二比特
        # 偶数情况 0 11110    假如说最后0前面有偶数个连续的1，那么最后一个必为一比特

        while bits and bits.pop(-1):
            res ^= 1

        # 假如说 ^= 偶数个1，res 依旧为0
        return res == 0

"""
Time: O(n) Space: O(1)
https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/solution/1bi-te-yu-2bi-te-zi-fu-by-leetcode/
没啥好说的，就是上面注释的规律
"""