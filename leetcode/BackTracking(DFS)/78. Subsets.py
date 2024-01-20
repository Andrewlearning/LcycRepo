"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.nums = nums
        self.res = []
        self.helper(0, [])
        return self.res

    def helper(self, startFrom, temp):
        self.res.append(temp[:])

        for i in range(startFrom, len(self.nums)):
            temp.append(self.nums[i])
            self.helper(i + 1, temp)
            temp.pop()

if __name__  == "__main__":
    solution = Solution()
    print(solution.subsets([1,2,3]))

"""
Time: O(2^n), Space: O(n)
- 因为答案最大长度为n，所以相当于最长的那个答案，对于每一位我们都可以进行选择是取还是不取，所以对于生成每一个答案的时间复杂度是2^n, 又因为往答案里添加第一个元素的for循环，需要循环n次，所以总体时间复杂度是 n*2^n
- 空间复杂因为递归深度最大为n，所以就为n
"""