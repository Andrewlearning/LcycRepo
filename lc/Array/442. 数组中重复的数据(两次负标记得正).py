"""
给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。
找到所有出现两次的元素。
你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？
示例：

输入:
[4,3,2,7,8,2,3,1]

输出:
[2,3]
"""

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            # 因为数字nums数组里数的范围是1~n
            # 下标是0 ~ n-1
            # 下标与num的映射是 index = num - 1
            # 一个数出现一次，则在它的对应下标上 *(-1), 这样遍历一次
            # 假如一个数出现两次，那么那个数所对应的下标上的数，肯定为正
            cur_index = abs(num) - 1

            # 把数组对应位置的元素变为负数
            nums[cur_index] *= -1


            # 假如说对应位置的数字是正数，说明被两个相同数字对应了，说明当前num是重复数字
            if nums[cur_index] > 0:
                # 把当前num加进res
                res.append(abs(num))

        return res

"""
https://www.acwing.com/video/1843/
思想与448相似
Time:O(n) space:O(n)
例如 [1,1,2]

num = 1, cur_index = 0, -> [-1,1,2]
num = 1, cur_index = 0, -> [1,1,2]
num = 2, cur_index = 1, -> [1,-1,2]

注意，这里我们不能把判断下标值 > 0 这部分，放在数组外重新执行
因为这个数组有重复数字，这就意味着肯定有数字没办法被 *(-1)
所以我们得走一步得判断一步，因为假如说那个数字出现两次了，在*(-1)当次循环中也是可以检测出来的
"""