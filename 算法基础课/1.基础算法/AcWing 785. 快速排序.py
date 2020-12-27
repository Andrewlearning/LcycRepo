def quickSort(nums, l, r):
    if l >= r:
        return

    # 偏移量
    i = l - 1
    j = r + 1
    pivot = nums[l + r >> 1]
    
    while i < j:
        # 从左边找到 >= pivot的数
        while True:
            i += 1
            if nums[i] >= pivot:
                break

        # 从右边找到 <= pivot的数
        while True:
            j -= 1
            if nums[j] <= pivot:
                break

        # 交换
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    # 记住这个模板
    # [l, j, j+1, r]
    quickSort(nums, l, j)
    quickSort(nums, j+1, r)

if __name__ == "__main__":
    n = int(input())
    nums = map(int, input().split(" "))

    quickSort(nums, 0, n-1)
    print(" ".join(map(str, nums)))

# https://www.acwing.com/activity/content/code/content/41595/
