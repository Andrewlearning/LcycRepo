class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 由于字符串中出现的字符的 ASCII 码在 0 到 127 之间，因此我们可以枚举所有的字符
        hashmap = [0] * 128

        count = 0

        for char in s:
            hashmap[ord(char) - ord("A")] += 1

            # 当字符出现偶数次时，count - 1
            if hashmap[ord(char) - ord("A")] % 2 == 0:
                count -= 1

            # 当字符出现奇数次时，count + 1
            else:
                count += 1

        return count <= 1

"""
时间复杂度：O(|S|)。我们只需要遍历一次字符串。
空间复杂度：O(128)。数组的长度为 128。

https://leetcode-cn.com/problems/palindrome-permutation/solution/hui-wen-pai-lie-by-leetcode/


"""

