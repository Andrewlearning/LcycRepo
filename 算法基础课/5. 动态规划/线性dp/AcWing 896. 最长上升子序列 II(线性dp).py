def searchInsert(nums, length, target):
    l = 0
    r = length

    while l < r:
        mid = (l + r) // 2

        if nums[mid] >= target:
            r = mid
        else:
            l = mid + 1

    return l


def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums is None:
        return []

    n = len(nums)
    res = [0] * n
    reslen = 0

    for x in nums:
        i = searchInsert(res, reslen, x)
        # 更新结果子串
        res[i] = x
        if i == reslen:
            reslen += 1
    return reslen


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(lengthOfLIS(nums))

# 本题使用而二分的解法
"""
时间复杂度O(NlongN) 空间复杂O（N），新开了一个list,二分查找是logN，比较强
答案：
这里的设计其实很巧妙，每次从nums取一个数出来，看它能在res
里放在什么位置，但都是按照从小往大的顺序（满足要求）

case 1,8,4,9...

例如：原来是[1,8],现在遍历到4
1.新遍历到的数字（4），可以插入的位置为res的最右边[1,x]，且[1,8],[1,4]长度相等，那么我们就把[1,8]替换成[1,4]
(最好的策略，为了找除最长字串）
2.新遍历到的数字（9）,可以插入的位置为len(res),[1,4]x,所以能增加res的长度，于是我们把9加进[1,4]->[1,4,9]

"""
