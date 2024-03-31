"""
pancake sort
给定一个数组，从1~n, 长度为n，未排序
让你每次只能从[0~x]这样完全翻转，最终使得能完成排序，要怎么做
"""
class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res = []
        length = curLargetst = len(arr)

        for i in range(length):
            # 找到arr未排序部分的最大值的下标
            index = self.findMax(arr, curLargetst)

            # 把未排序的最大值翻转到index=0
            self.flip(arr, index)

            # 把未排序的最大值翻转到index=未排序的最末端
            self.flip(arr, curLargetst - 1)

            # 这两步说实话不知道在干啥
            res.append(index + 1)
            res.append(curLargetst)

            # 更新未排序的最大值，便于下一次进行操作
            curLargetst -= 1

        # 输出后我们发现arr已经排序好了
        print(arr)
        return res

    # 找到当前未排序部分的最大的元素的下标
    def findMax(self, arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1

    # 从0~index整个反转数组
    def flip(self, arr, index):
        i = 0
        j = index
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

"""
# O(n+k) 古城算法 这个做法比较好，桶排序
# https://www.bilibili.com/video/BV1G54y1a7gS
"""