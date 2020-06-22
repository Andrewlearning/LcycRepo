class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1

        # 为什么这里不是 <= 呢
        # 因为假如说是 <= 遇到单边递增的情况，我们下面的mid+1就会out of range
        # [0,1,2,3]
        # 因为r一直是len - 1 = 3
        # 这种情况当然是一直是l = mid + 1
        # 当最后到 l = r = 3的时候，说明已经到最右边的元素了，已经不满足l<r了
        # 所以会退出循环，返回l
        # 同理，递减的情况，[4,3,2,1]也是
        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            
            elif nums[mid] < nums[mid - 1]:
                r = mid - 1
            else:
                return mid

        # 其实这里返回l,或者是r，关系都不大，原因看上面
        # 因为当最大值在任意一边的时候，l,r的退出循环时候的值都是一样的162. 寻找峰值
        return l


"""
我们把它看成一个，上坡或者下坡的过程就好了，一直往上坡的方向走
"""