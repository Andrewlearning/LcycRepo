"""
摇摆序列就是一大一小一大一小这样的，求出一个最大的摇摆序列
Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].（可以跳着来找的，不一定要连续的）

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
"""
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 把连续相同的字母，只留下一个
        p = 1
        while p < len(nums):
            if nums[p - 1] == nums[p]:
                nums.pop(p)
                continue
            p += 1

        if len(nums) <= 2:
            return len(nums)

        # 我们默认把开头结尾先算进去，假如说只有开头结尾的话
        # 那么它一定是摆动的，因为我们已经去重了
        res = 2

        for i in range(1, len(nums) - 1):
            a = nums[i - 1]
            b = nums[i]
            c = nums[i + 1]
            # 因为我们已经去重了，那么假如b满足摆动的条件，那么我们++就好了
            if (a > b and c > b) or (a < b and c < b):
                res += 1

        return res


# https://www.acwing.com/video/1760/


