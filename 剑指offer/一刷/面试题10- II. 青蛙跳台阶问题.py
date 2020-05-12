class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            res = [0]*(n+1)
            res[0] = 0
            res[1] = 1
            res[2] = 2

            for i in range(3,n+1):
                res[i] = res[i-1] + res[i-2]

            return res[-1] % 1000000007





if __name__ == "__main__":
    solution = Solution()
    solution.jumpFloor(3)

