"""
中给出一个 n_rows 行 n_cols 列的二维矩阵，且所有值被初始化为 0。要求编写一个 flip 函数，均匀随机的将矩阵中的 0 变为 1，并返回该值的位置下标 [row_id,col_id]；同样编写一个 reset 函数，将所有的值都重新置为 0。尽量最少调用随机函数 Math.random()，并且优化时间和空间复杂度。

注意:

1 <= n_rows, n_cols <= 10000
0 <= row.id < n_rows 并且 0 <= col.id < n_cols
当矩阵中没有值为 0 时，不可以调用 flip 函数
调用 flip 和 reset 函数的次数加起来不会超过 1000 次
示例 1：

输入:
["Solution","flip","flip","flip","flip"]
[[2,3],[],[],[],[]]
输出: [null,[0,1],[1,2],[1,0],[1,1]]
"""

import random
class Solution:

    def __init__(self, n_rows, n_cols):
        self.num = n_rows * n_cols
        self.n_rows = n_rows
        self.n_cols = n_cols

        # 正常来说，下标0寸的数是0，下标1存的数是1
        # 但假如说有数被取出来过，对应下标的数可能就发生了修改，这个map就记录这些被修改过的数
        # key:index value:value
        self.lookup = {}

    def flip(self):
        self.num -= 1
        # 随机得到的下标
        x = random.randint(0, self.num)

        # 得到y， y是x位置上的值
        y = x
        if x in self.lookup:
            y = self.lookup[x]

        # 下一步要把y删掉，用最后位置上的数一个元素代替到x的位置
        # 先判断最后一个位置上的数是特殊值
        if self.num in self.lookup:
            # 然后把最后一个位置上的数覆盖到x上
            self.lookup[x] = self.lookup[self.num]
            # 然后把最后一个位置上的数删掉，因为再也不会用到了
            del self.lookup[self.num]

        # 先判断最后一个位置上的数是正常值，self.lookup[x]直接等于
        else:
            self.lookup[x] = self.num

        return [y // self.n_cols, y % self.n_cols]

    # 恢复所有设置，包括hashmap和self.num
    def reset(self):
        self.lookup.clear()
        self.num = self.n_cols * self.n_rows

"""
把一个矩阵拉成一个数组，然后随机在数组里取一个数，被取出的数下次不能再取，于是用数组最后一个元素进行替换
返回被取出数的横纵下标
https://www.acwing.com/video/1928/
"""
