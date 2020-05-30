"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []

        self.res = []

        # 处理重复记得先排序
        candidates.sort()
        self.helper(candidates, target, 0, [])
        return self.res

    def helper(self, candidates, target, idx, temp):
        if target < 0:
            return

        if target == 0:
            self.res.append(temp[:])

        for i in range(idx, len(candidates)):
            # 关键的处理在这里，因为idx绝对是一个新的下标，所以我们要遍历到
            # 同时我们要判断重复，且要保证能完整遍历完整个数组，所以要用一个i > idx
            if i > idx and candidates[i - 1] == candidates[i]:
                continue

            self.helper(candidates, target - candidates[i], i + 1, temp + [candidates[i]])


"""
https://www.youtube.com/watch?v=5ybHmOt3-34
注意：
处理办法，与subset,combination那些去重复的差不多。
1.nums先排序 2.然后不让candidates[i] == candidates[i-1]

"""