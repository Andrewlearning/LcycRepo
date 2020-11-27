"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2} 为 {1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

"""
class Solution(object):
    def minArray(self, nums):
        """
        :type numbers: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0

        l = 0
        r = len(nums) - 1

        while l < r:

            mid = (l + r) // 2

            # mid 的右边一定又最小数字
            # 所以我们要 [mid+1, r]这个区间
            if nums[mid] > nums[r]:
                l = mid + 1

            # 说明 mid,right 在小区间，那么我们要慢慢缩小范围把范围变到[l,r-1]
            elif nums[mid] == nums[r]:
                r = r - 1

            # mid 的右边一定不是最小数字，mid 有可能是, mid的左边可能是，下一轮搜索区间是[left, mid]
            elif nums[mid] < nums[r]:
                r = mid

        # 这里放l,r都无所谓, 为什么
        return nums[l]


"""
https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solution/er-fen-jian-zhi-si-xiang-fen-zhi-si-xiang-by-liwei/
"""