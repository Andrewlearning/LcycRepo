"""
给定一个无重复元素的数组candidates和一个目标数target
找出candidates中所有可以使数字和为target的组合。
candidates中的数字可以无限制重复被选取。
* candidates是有序的


说明：

所有数字（包括target）都是正整数。
解集不能包含重复的组合。
示例1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.nums = candidates
        self.target = target
        self.res = []
        self.temp = []
        self.helper(0)
        return self.res

    def helper(self, start):
        if sum(self.temp) > self.target or start >= len(self.nums):
            return

        if sum(self.temp) == self.target:
            self.res.append(self.temp[:])
            return

        for i in range(start, len(self.nums)):
            self.temp.append(self.nums[i])
            # 每个位置上的数都可以被选取无数次，所以下一次依旧可以从这里开始
            self.helper(i)
            self.temp.pop()


"""
为什么这里需要 start，因为假如[1,2,3] target=6
假如没有start的话，会产生[1,2,3] [2,1,3] [3,1,2]这三个结果，对于本题来说是重复的
所以我们为了防止选取到相同的组合，我们得限制不能一直选取的范围
"""
