"""
输入:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
输出:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
解释:
对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
"""

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        lr = len(M)
        lc = len(M[0])

        res = [[0 for c in range(lc)] for r in range(lr)]

        for r in range(lr):
            for c in range(lc):
                count = 0

                for nr in (r - 1, r, r + 1):
                    for nc in (c - 1, c, c + 1):
                        if 0 <= nr < lr and 0 <= nc < lc:
                            res[r][c] += M[nr][nc]
                            count += 1

                res[r][c] //= count

        return res

"""
时间复杂度：O(N)，其中N 是图片中像素的数目。我们需要将每个像素都遍历一遍。
空间复杂度：O(N)，我们答案的大小。

https://leetcode-cn.com/problems/image-smoother/solution/tu-pian-ping-hua-qi-by-leetcode/
就对边界情况处理一下，当出界时，就不添加它

"""

