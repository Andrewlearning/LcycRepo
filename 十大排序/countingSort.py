class Solution(object):
    def countingSort(self, arr):
        n = len(arr)
        output = [0] * n
        count = [0] * 256

        for num in arr:
            count[num] += 1

        for i in range(256):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            output[count[arr[i]] - 1] = arr[i]
            count[arr[i]] -= 1

        for i in range(n):
            arr[i] = output[i]

        print(output)


if __name__ == '__main__':
    s = Solution()
    s.countingSort([1, 4, 1, 2, 7, 5, 2])

"""
古城算法
T:O(n+k)
https://www.bilibili.com/video/BV1G54y1a7gS

1,4,1,2,7,5,2
1. 先把所有数出现的次数记录在count的对应下标里
index: 0,1,2,3,4,5,6,7,8,9
count: 0,2,2,0,1,1,0,1,0,0

2.计算count的前缀和
index: 0,1,2,3,4,5,6,7,8,9
count: 0,2,4,4,5,6,6,7,7,7

3.根据前缀和给数字排序
例如1的前缀和是2，那么1就排在count[arr[i]] - 1] -> 0，1这两个位置
例如2的前缀和是4，那么2就排在count[arr[i]] - 1] -> 2，3这两个位置
"""