def merge_sort(arr, l, r, temp):
    if l >= r:
        return
    # 1.选取中点
    mid = (l + r) // 2
    # 2.递归排序
    merge_sort(arr, l, mid, temp)
    merge_sort(arr, mid + 1, r, temp)

    # 3.归并操作，原数组的左右两半指针
    i = l
    j = mid + 1

    # temp数组的指针
    k = 0
    while (i <= mid and j <= r):
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= r:
        temp[k] = arr[j]
        j += 1
        k += 1
    
    # temp记录排序好的数组
    # 然后更新到原数组上
    i, j = l, 0
    while i <= r:
        arr[i] = temp[j]
        i += 1
        j += 1


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    temp = [0] * n
    merge_sort(lst, 0, len(lst) - 1, temp)
    print(' '.join(map(str, lst)))


# 链接：https://www.acwing.com/activity/content/code/content/111492/
