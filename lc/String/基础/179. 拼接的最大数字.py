"""
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:
Input: [10,2]
Output: "210"

Example 2:
Input: [3,30,34,5,9]
Output: "9534330"
"""


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if max(nums) == 0: return "0"

        nums = list(map(str,nums))
        from functools import cmp_to_key
        nums.sort(key = cmp_to_key(lambda a,b: 1 if a+b < b+a else -1))
        return "".join(nums)


"""
https://blog.csdn.net/qq_39843857/article/details/85263280
答案：
1.这里需要用到字符串的比较 "9" > "88"(只看第一个数)
                        "91" < "99" (第一数相同看第二个数。。一次类推）

cmp_to_key的用法就是，返回1的话，那就按a,b排
                    返回-1的话，那就按b,a排

"""


