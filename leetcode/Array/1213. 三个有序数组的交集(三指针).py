"""
给出三个均为 严格递增排列 的整数数组 arr1，arr2 和 arr3。
返回一个由 仅 在这三个数组中 同时出现 的整数所构成的有序数组。

示例：
输入: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
输出: [1,5]
解释: 只有 1 和 5 同时在这三个数组中出现
"""
class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        res = []
        p1, p2, p3 = 0, 0, 0
        while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
            if arr1[p1] == arr2[p2] == arr3[p3]:
                res.append(arr1[p1])
                p1 += 1
                p2 += 1
                p3 += 1
            else:
                # 这里三指针的变化适用于调整他们的大小，使得指针挪动到能满足
                # arr1[p1] == arr2[p2] == arr3[p3] 这种情况
                if arr1[p1] <= arr2[p2] and arr1[p1] <= arr3[p3]:
                    p1 += 1
                elif arr2[p2] <= arr1[p1] and arr2[p2] <= arr3[p3]:
                    p2 += 1
                elif arr3[p3] <= arr1[p1] and arr3[p3] <= arr2[p2]:
                    p3 += 1
        return res

"""
https://leetcode-cn.com/problems/intersection-of-three-sorted-arrays/solution/san-zhi-zhen-fa-by-mnm135/

本题做法等于是350排序双指针做法的翻版， 等于是三指针
"""


