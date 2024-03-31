class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # 杨辉三角第k行，实际上就是第k+1行，所以我们要创建有k+1长度的数组
        res = [0 for i in range(rowIndex + 1)]

        # 每一行的最左边在这里已经定义了
        res[0] = 1

        # 这个赋值过程要重复 rowIndex + 1次
        for i in range(rowIndex + 1):

            # 当前回合的最右元素定为1
            res[i] = 1
            # j的活动范围是[1,j-1]
            j = i - 1

            # j > 0, 使得j在边界[1,j-1]之间移动
            # 1
            # 1  1
            # j-1 j  1
            while j > 0:
                res[j] = res[j] + res[j - 1]
                j -= 1

        return res


"""
Time: O(k^2), Space: O(1)
https://algocasts.io/episodes/D1mR10Wz

相对于118 帕斯卡三角
我们这题则更追求一种空间上的压缩

 1 
 1    1
 j-1  j  1
"""
