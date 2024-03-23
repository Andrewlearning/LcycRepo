class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]
            if s > target:
                r -= 1
            elif s < target:
                l += 1
            else:
                return [l + 1, r + 1]

        return []

"""
Time: O(n), Space: O(1)
https://www.acwing.com/video/1545/
答案：
因为是排序的，所以直接用双指针来做。时间空间效率最高
"""