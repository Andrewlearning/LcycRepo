"""
把一个无序且有重复的数组 变成一个 摇摆序列
这里的摇摆序列指的是，奇数位比偶数位大
"""


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums and len(nums) == 0: return []

        sortedlist = sorted(nums)
        n = len(nums)
        small = (n - 1) // 2
        large = n - 1

        for i in range(n):
            # 偶数的时候要填比较小的
            if i % 2 == 0:
                nums[i] = sortedlist[small]
                small -= 1
            # 奇数是要填比较大的
            else:
                nums[i] = sortedlist[large]
                large -= 1


"""
https://www.youtube.com/watch?v=48AAAx30zNY
答案：
1.提交要求一定要in-place,所以就取消了使用res的数组，直接使用一个新数组来记录排序后的nums
2.这题的做法其实有很难得，但是目前只学习一下简单的做法把
  我们首先先把数组排序好 【1,1,1,4,5,6】
  left = (6-1)//2 = 2
  right = 5
  然后创建两个指针left,right, left指向中点，right指向最后
  然后我们按照顺序，left-right-left-right这样的，把元素按顺序插入到nums里面去
  
  那么数组有奇数个数字呢？[1,1,1,1,4,5,6]
  还是一样的，left = (7-1)//2 = 3
             right = 6
             所以结果会是[1,6,1,5,1,4,1]
             依旧满足摇摆序列
"""
