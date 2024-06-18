"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        # 排序一下，因为后面需要对比重复
        nums.sort()
        # 这属于一个比较通用的解法，因为在全排序2会碰到有相同元素的情况
        # 在那个时候就不太适合用一个 set去储存元素了
        visited = [False] * n

        def dfs(n, temp):
            if len(temp) > n:
                return

            if len(temp) == n:
                res.append(temp[:])
                return

            for i in range(n):
                # 过滤掉已经使用过的元素
                if visited[i]:
                    continue
                # 过滤掉使用过，且重复的元素
                if i > 0 and visited[i-1] == True and nums[i] == nums[i-1]:
                    continue
                temp.append(nums[i])
                visited[i] = True
                dfs(n, temp)
                visited[i] = False
                temp.pop()

        dfs(n, [])
        return res

"""
"""