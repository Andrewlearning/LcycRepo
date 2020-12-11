class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1


        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            
            elif nums[mid] < nums[mid - 1]:
                r = mid - 1
            # 这只能判断 [mid-1] < mid > [mid+1] 这种情况
            # 但判断不了[0,1,2,3]这种单边递增的峰值
            # 所以循环到最后会收敛到l = r
            else:
                return mid

        # 其实这里返回l,或者是r，关系都不大，因为退出循环必然是l = r
        # 因为当最大值在任意一边的时候，l,r的退出循环时候的值都是一样的162. 寻找峰值
        return l


"""
我们把它看成一个，上坡或者下坡的过程就好了，一直往上坡的方向走
"""