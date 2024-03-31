"""
Given an array nums of n integers and an integer target, are there elements a, b, c,
 and d in nums such that a + b + c + d = target?
 Find all unique quadruplets（四胞胎） in the array which gives the sum of target.

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        first = 0

        for first in range(len(nums) - 3):
            if first > 0 and nums[first - 1] == nums[first]:
                continue

            for second in range(first + 1, len(nums) - 2):
                if second > first + 1 and nums[second - 1] == nums[second]:
                    continue

                l = second + 1
                r = len(nums) - 1

                while l < r:
                    temp = [nums[first], nums[second], nums[l], nums[r]]
                    total = sum(temp)

                    if total == target:
                        res.append(temp)
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r - 1] == nums[r]:
                            r -= 1
                        l += 1
                        r -= 1

                    elif total > target:
                        r -= 1
                    else:
                        l += 1
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.fourSum([-3,-2,-1,0,0,1,2,3],0))

"""
https://www.youtube.com/watch?v=YkxsyPItHeM
这题最好不要按照algocast的写法来写，因为java的for 和python 的for range的语法处理效果不同
建议按照自己的3sum的版本来写
3sum是定一个指针，移动两个指针，4sum是定两个指针，移动两个指针

注意：
每个for循环下一定要注意判断重复！！
"""