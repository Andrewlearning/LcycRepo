"""
索引从0开始长度为N的数组A，包含0到N - 1的所有整数。找到最大的集合S并返回其大小，其中 S[i] = {A[i], A[A[i]], A[A[A[i]]], ... }且遵守以下的规则。

假设选择索引为i的元素A[i]为S的第一个元素，S的下一个元素应该是A[A[i]]，之后是A[A[A[i]]]... 以此类推，不断添加直到S出现重复的元素。

 

示例 1:

输入: A = [5,4,0,3,1,6,2]
输出: 4
解释:
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

其中一种最长的 S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
"""
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(nums)):
            # 假如nums[i]未被标记过，说明nums[i]不在之前
            # 任意形成的一个环内
            if nums[i] != -1:
                j = i
                temp = 0
                # 把nums[i]能到的节点组成一个环，计算环的长度
                while nums[j] != -1:
                    temp += 1
                    next = nums[j]
                    # 使用nums[j]构成新环，然后将它标记，不被下次使用
                    nums[j] = -1
                    # 讲j移动到下一个位置
                    j = next

            res = max(res, temp)

        return res

# https://www.acwing.com/video/2034/
