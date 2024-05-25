"""
Given an array nums of n integers, are there elements a, b, c
in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return

        res = []
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            #查看当前的nums[i]和上一个index是否相同，如相同则跳过，因为会产生相同的结果
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1 ,n-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res.append([nums[i],nums[l],nums[r]])

                    """
                        在这层做判断是，假如数字l, r移动到下一位的数字还是相同的话，会再次进入这个判断
                        记录一次重复的答案
                        
                        假如说当前循环left,right左右都有相同元素，则进行一次去重处理，不然会返回相同结果
                        例如 1,2,3,3,3,4 那么这个left最终会停留到最后一个3， 因为[3,4]是不相同的
                    """
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    # 同理这个 1,2,3,3,3,4 这个right最终会停留到最左的一个3，因为[2,3]不同
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1

                    #res已经append了当前这个重复数字，当前我们的l,r还停留在最后一个重复数字上
                    #所以我们最后要移动一下
                    #直到执行完下一步操作left,right才摆脱重复数字
                    l += 1
                    r -= 1
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-3,-2,0,1,2,5]))


"""
答案：  
3.sort and find(two pointer) 
  1。首先先把数组sort一遍，O(nlogn)
  2。开始遍历数组，定遍历的指针为index,[index,-1,0,1,2,3]
  3。然后创建两个指针，left是index右的第一个元素，right是列表最后一个元素
  3。开始一个while 循环，当 index + left + rigth > 0时，right左移，反之left右移
  4。找到返回true,没找到推出循环返回false
  两个循环 O（n^2)

"""