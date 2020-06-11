"""
Given two sorted integer arrays nums1 and nums2,
merge nums2 into nums1 as one sorted array.(要求在nums1里inplace sort完成)
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        p = m + n - 1
        p1 = m - 1
        p2 = n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p -= 1
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p -= 1
                p2 -= 1

        while p1 >= 0:
            nums1[p] = nums1[p1]
            p -= 1
            p1 -= 1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1

        return nums1

"""
// Time: O(m+n), Space: O(1)
答案:
1.inplace 交换，所以s是O(1)
2.leetcode都帮用户准备好了，nums1自动加长了，假如说没有加长，我们需要
  nums1 + [0]*len(nums2)
3.我们用指针k来维护新数组，用i,j来遍历老数组,k,i,j三个指针都分别的数组的后面往前
查找比较，节省时空间复杂度
4.最后假如说那个数组有剩下的，就把它全部替换到答案数组里面去，操作像merge sort
"""