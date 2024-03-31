"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
"""


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(int(c ** 0.5) + 1):
            j = c - i ** 2
            sqrtJ = int(j ** 0.5)
            if sqrtJ ** 2 == j:
                return True

        return False





"""
# Time: O(c ^ 1 / 2), Space: O(1)
https://www.acwing.com/video/2129/
"""
