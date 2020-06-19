"""
比如说，给你的数字是 5，你要返回帕斯卡三角形的前 5 行。

     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if not numRows or numRows == 0:
            return []

        res = []

        for i in range(numRows):
            # 第0行有一个元素，第1行有一个元素，第2行有三个元素
            # 我们等于先把要处理的行 先初始化
            # 且该行的头尾都为1, 这个也要初始化
            temp = [1 for _ in range(i + 1)]

            # 第一轮,res = [], range(1,1)等于不用操作了
            # 所以头尾的1 我们就不用进行操作了
            # 然后当前的 [j] = [j-1] + [j]
            for j in range(1, len(temp) - 1):
                temp[j] = res[i - 1][j - 1] + res[i - 1][j]

            res.append(temp)

        return res

"""
https://algocasts.io/episodes/jwmBr5m8
Time: O(n^2), Space: O(1)
"""