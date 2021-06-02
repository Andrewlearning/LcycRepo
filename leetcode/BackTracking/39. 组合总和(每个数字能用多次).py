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
        if not candidates:
            return []

        self.res = []
        self.helper(candidates, target, 0, [])
        return self.res

    def helper(self, candidates, target, idx, temp):
        if target < 0:
            return

        if target == 0:
            self.res.append(temp[:])

        # candidates 中的数字可以无限制重复被选取, 所以这里的的idx不用变成range(idx+1, ..)
        for i in range(idx, len(candidates)):
            self.helper(candidates, target - candidates[i], i, temp + [candidates[i]])


"""
https://www.youtube.com/watch?v=zIY2BWdsbFs
eg[2,3,6,7] t = 7
注意：这里的target为什么减完后不需要还原？
因为对于同一个for 循环来说，每个target都是相同的，意思就是说，假如说candidate[i] = 2,那么就是从2开始往下找
                                            同样的，对于candiditaes[i] = 7来说，也是从7开始往下找，所以
                                            大家机会都一样，不需要对target进行任何操作
                                            
1.组合，意味着无序，假如说，[1,1,3],[3,1,1],[1,3,1]对于组合来说是相同的，所以我们只用传里面的一个答案就好
  但对于permutation 是不同的。所以permutation 要用一个used来记载当前使用着哪个元素。
  所以对待组合题目，我们传递helper的时候，应该是传递candidates的index，使得之前已经被传递过的数，不应该被
  再次传递
2.同时因为这题是允许重复的，所以我们传参数，不需要传i+1, 只用传i就好了

剪枝：
1. if target < 0: return . 因为已经不能满足题目条件了，所以我们遇到这种情况直接return 
2. 我在helper的 for里面增加了剪枝，只要有可能出现 target - candidate[i] < 0,的直接省略

"""
