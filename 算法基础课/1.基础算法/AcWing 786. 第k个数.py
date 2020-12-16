"""
找出一个无序数组第k小的数

"""

def quick_select(nums, l, r, k):
    if l >= r:
        return nums[l]

    pivot = nums[l]
    i = l - 1
    j = r + 1
    while i < j:

        while True:
            i += 1
            if nums[i] >= pivot:
                break

        # 从右边找到 <= pivot的数
        while True:
            j -= 1
            if nums[j] <= pivot:
                break

        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    lenj = j - l + 1

    if k <= lenj:
        return quick_select(nums, l, j, k)
    return quick_select(nums, j + 1, r, k - lenj)


if __name__ == '__main__':
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    res = quick_select(nums, 0, n - 1, k)
    print(res)

# https://www.acwing.com/video/228
# 链接：https://www.acwing.com/solution/content/21773/
