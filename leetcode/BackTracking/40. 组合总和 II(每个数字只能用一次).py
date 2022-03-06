"""
给定一个数组candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。

candidates中的每个数字在每个组合中只能使用一次。
candidates是是无序的

与第 39 题（组合之和）的差别

这道题与上一问的区别在于：
第 39 题：candidates 中的数字可以无限制重复被选取；
第 40 题：candidates 中的每个数字在每个组合中只能使用一次。
相同点是：相同数字列表的不同排列视为一个结果。


说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。
示例1:

输入: candidates =[10,1,2,7,6,1,5], target =8,
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

    def helper(self, candidates, target, cur, temp):
        if sum(temp) > target:
            return

        if sum(temp) == target:
            self.res.append(temp[:])
            return

        for i in range(cur, len(candidates)):
            # 一个for循环，意味着一层递归
            # 为了避免[1,1,7] 变成 [1,7], [1,7]重复的话，需要保证在同一层递归中没有重复元素
            # i > cur是因为保证 1.保证不会数组越界 2.假如i>0,有可能出现误删，因为有可能前一个数是上一次循环的结果，
            # 并不在同一层递归中
            if i > cur and candidates[i - 1] == candidates[i]:
                continue

            temp.append(candidates[i])
            self.helper(candidates, target, i + 1, temp)
            temp.pop()

"""
https://www.youtube.com/watch?v=5ybHmOt3-34
注意：
处理办法，与subset,combination那些去重复的差不多。
1.nums先排序 2.然后不让candidates[i] == candidates[i-1]

"""