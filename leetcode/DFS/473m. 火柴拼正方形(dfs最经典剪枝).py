"""
还记得童话《卖火柴的小女孩》吗？现在，你知道小女孩有多少根火柴，请找出一种能使用所有火柴拼成一个正方形的方法。不能折断火柴，可以把火柴连接起来，并且每根火柴都要用到。

输入为小女孩拥有火柴的数目，每根火柴用其长度表示。输出即为是否能用所有的火柴拼成正方形。

示例 1:

输入: [1,1,2,2,2]
输出: true

解释: 能拼成一个边长为2的正方形，每边两根火柴。
示例 2:

输入: [3,3,3,3,4]
输出: false

解释: 不能用所有火柴拼成一个正方形。
"""

class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) == 0:
            return False

        self.nums = nums
        self.used = [False for i in range(len(nums))]

        # 看所有火柴的和有没有能不能被4整除
        sums = sum(nums)
        if sums % 4 != 0:
            return False

        sums /= 4
        # 排序，方便剪枝
        nums.sort()

        # 当前枚举的第一根火柴，当前的长度，每条边的总长度，当前正方形拼到第几根
        return self.helper(0, 0, sums, 0)

    def helper(self, start, curLength, length, cnt):
        # 假如说已经拼到了第四根，说明前三根都拼出来了，说明没问题了
        if cnt == 3:
            return True

        # 说明当前边拼接成功，开始拼下一根
        if curLength == length:
            return self.helper(0, 0, length, cnt + 1)

        i = start
        while i < len(self.nums):
            # 假如当前这根火柴用过了，跳过
            if self.used[i] is True:
                i += 1
                continue

            if curLength + self.nums[i] <= length:
                self.used[i] = True
                if self.helper(i + 1, curLength + self.nums[i], length, cnt):
                    return True
                # 找不到，回溯
                self.used[i] = False


            # 剪枝，假如是第一根火柴或者是最后一根火柴，不用再往下回溯
            # curLength=0 说明当前失败的是第一根火柴，因为已拼成长度为0，假如说当前最短的火柴，匹配后面所有的解
            # 都配不出来的话，那么其他火柴更赔不起来

            # curLength + self.nums[i] == length失败的是一条边的最后一根火柴
            # 这根火柴可以拼成一条边，但是在上面的回溯却失败了，那说明用这条边的话，是没办法得出一个解的
            if not curLength or curLength + self.nums[i] == length:
                return False

            # 剪枝，假如说当前边不能成功回溯，那么与当前火柴相同长度的火柴肯定也不能成功，跳过
            while i + 1 < len(self.nums) and self.nums[i+1] == self.nums[i]:
                i += 1

            i += 1

        return False


# https://www.acwing.com/video/1881/