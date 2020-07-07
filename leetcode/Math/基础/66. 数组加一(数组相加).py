"""
Given a non-empty array of digits representing a non-negative
 integer, plus one to the integer.
Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        digits[-1] += 1
        carry = 0

        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            carry = 0

            if digits[i] >= 10:
                digits[i] -= 10
                carry = 1

        if carry:
            digits.insert(0, carry)

        return digits

"""
time:On space O1
https://www.youtube.com/watch?v=6A-DTVB9HT8
"""
