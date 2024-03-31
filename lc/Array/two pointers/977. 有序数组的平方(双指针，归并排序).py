class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # 作为负数的分界线
        negative = -1
        for i in range(len(nums)):
            if nums[i] < 0:
                negative = i
            else:
                break

        n = len(nums)
        res = []
        # 负数区域是从后往前升序
        i = negative
        # 整数区域是从前往后升序
        j = negative + 1

        # 这里做一个归并排序
        while i >= 0 or j < n:
            # i已经遍历完了
            if i < 0:
                res.append(nums[j] ** 2)
                j += 1
            # j已经遍历完了
            elif j == n:
                res.append(nums[i] ** 2)
                i -= 1
            # 放小的进res
            elif nums[i] ** 2 < nums[j] ** 2:
                res.append(nums[i] ** 2)
                i -= 1
            else:
                res.append(nums[j] * nums[j])
                j += 1

        return res