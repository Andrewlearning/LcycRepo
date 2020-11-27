"""
统计一个数字在排序数组中出现的次数。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            return 0

        left = self.findleft(nums, target)
        right = self.findright(nums, target)

        return right - left + 1

    def findleft(self, nums, target):
        l = 0
        r = len(nums) - 1
        index = -1

        # 都是左闭右闭的写法
        while l <= r:
            mid = (l + r) // 2

            # 关键点在这里， 当num == target的时候， 要把区间向左缩小
            if nums[mid] == target:
                r = mid - 1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1

            # 每次循环完，检查便看是否可以更新index
            if nums[mid] == target:
                index = mid

        return index

    def findright(self, nums, target):

        l = 0
        r = len(nums) - 1
        index = -1

        # 都是左闭右闭的写法
        while l <= r:
            mid = (l + r) // 2
            # 关键点在这里， 当num == target的时候， 要把区间向右缩小
            if nums[mid] == target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1

            # 每次循环完，检查便看是否可以更新index
            if nums[mid] == target:
                index = mid

        return index


if __name__ == "__main__":
    solution = Solution()
    solution.GetNumberOfK([1,2,2,3,3,3,5,6,7,8,8,8],8)



"""
感觉这个题应该想让你找到一个最快的算法吧
为什么直觉就是二分查找
可是问题来了，当你用二分查找找到以后，要怎么统计他出现的次数呢？
从对应index来前后查
然后后-前


额，这题我原来的做法也是可以，但是现在用的这个做法比较好一点
刚好能看出来二分查找的不同形式


"""