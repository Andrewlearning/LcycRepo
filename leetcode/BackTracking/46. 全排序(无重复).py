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
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        self.res = []

        # 这属于一个比较通用的解法，因为在全排序2会碰到有相同元素的情况
        # 在那个时候就不太适合用一个 set去储存元素了
        self.visited = [False] * len(nums)
        self.helper(nums, -1, [])

        return self.res

    def helper(self, nums, idx, temp):
        if len(temp) > len(nums):
            return

        if len(temp) == len(nums):
            self.res.append(temp[:])

        for i in range(len(nums)):

            # 假如当前下标还没被访问过, 那我们则进去
            if self.visited[i] == False:
                self.visited[i] = True
                self.helper(nums, i, temp + [nums[i]])
                self.visited[i] = False

        return

"""
https://www.youtube.com/watch?v=zIY2BWdsbFs
Time: O(n*n!), Space: O(n)
答案：
例子num = [1,2,3]
1.我们把nums的数字一个个放进去尝试，第一放1, 然后尝试1,(1,2,3),发现1在里面了，所以只有可能[1,2],[1,3]
2.[1,2]再尝试(1,2,3),发现只有3可以，所以生成123
3.[1,3]尝试（1,2,3),发现只有2可以，所以生成132
4.123,132完成后，把最后一位给pop（）掉，变成12,13,发现还是执行完了，再把最后一位给pop，变成1，最后1被pop()
5.开始执行以2为首的数

"""
