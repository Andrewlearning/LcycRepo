def quick_sort(nums, l, r):
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
    # [l, i-1, i, r]
    # [l, j, j+1, r]
    quick_sort(nums, l, j)
    quick_sort(nums, j+1, r)

if __name__ == '__main__':
    n = input()
    list_str = input()
    nums = list(map(int, list_str.split(" ")))
    quick_sort(nums, 0, len(nums) - 1)
    print(" ".join(map(str,nums)))


# https://www.acwing.com/activity/content/code/content/41595/
