"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        # 这属于一个比较通用的解法，因为在全排序2会碰到有相同元素的情况
        # 在那个时候就不太适合用一个 set去储存元素了
        visited = [False] * n

        def dfs(temp):
            if len(temp) > n:
                return

            if len(temp) == n:
                res.append(temp[:])
                return

            for i in range(n):
                # 过滤掉已经使用过的元素
                if visited[i]:
                    continue
                temp.append(nums[i])
                visited[i] = True
                dfs(temp)
                visited[i] = False
                temp.pop()

        dfs([])
        return res


"""
https://www.youtube.com/watch?v=zIY2BWdsbFs
- 时间复杂度 O(n×n!)
    - 因为我们总是先从n个元素中选择一位，然后在从n-1个元素中选择下一位，最终遍历完所有结果，所以时间复杂度是n!, 最后把路径结果list添加到res, append list需要O(n), 所以总体时间复杂度是 O(n * n!)
- 空间复杂度 O(n)
    - dfs的时候，空间复杂度取决于递归栈的深度。
    - 在最差情况下，有n个节点，调用栈最深是O(n)，
答案：
例子num = [1,2,3]
1.我们把nums的数字一个个放进去尝试，第一放1, 然后尝试1,(1,2,3),发现1在里面了，所以只有可能[1,2],[1,3]
2.[1,2]再尝试(1,2,3),发现只有3可以，所以生成123
3.[1,3]尝试（1,2,3),发现只有2可以，所以生成132
4.123,132完成后，把最后一位给pop（）掉，变成12,13,发现还是执行完了，再把最后一位给pop，变成1，最后1被pop()
5.开始执行以2为首的数


排列组合的区别：
组合 combination: 不强调顺序性 例如 [1,2] = [2,1]
排列 permutation: 强调顺序性   例如 [1,2] != [2,1] 这是两种结果
"""
