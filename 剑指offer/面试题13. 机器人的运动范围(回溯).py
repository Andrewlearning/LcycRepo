class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        self.visited = set()
        self.helper(0, 0, m, n, k)
        return len(self.visited)

    def helper(self, i, j, m, n, k):

        # 不单单要判断是否越界，是否重复，还要判断位数是否 > k
        if i >= m or j >= n or (i, j) in self.visited or (self.digitsum(i) + self.digitsum(j)) > k:
            return

        self.visited.add((i, j))

        # 我们试着联想一下可以发现，我们在每个格子都向右和向下走，就已经可以走完所有的格子了
        self.helper(i + 1, j, m, n, k)
        self.helper(i, j + 1, m, n, k)

    # 这个函数用来求每个的位数之和
    def digitsum(self, num):
        res = 0
        while num:
            res += num % 10
            num //= 10

        return res

    # https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/bfs-by-z1m/