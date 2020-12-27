def merge_sort(arr, l, r, temp):
    if l >= r:
        return
    # 1.选取中点
    mid = (l + r) // 2
    # 2.递归排序
    merge_sort(arr, l, mid, temp)
    merge_sort(arr, mid + 1, r, temp)

    # 把变量全局化
    global res
    # 3.归并操作，原数组的左右两半指针
    i = l
    j = mid + 1

    # temp数组的指针
    k = 0
    while (i <= mid and j <= r):
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        # [i] > [j], 所以[i-mid]都比[j]大
        else:
            temp[k] = arr[j]
            res += mid - i + 1
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
    array = list(map(int, input().split()))
    temp = [0] * n
    res = 0
    merge_sort(array, 0, len(array) - 1, temp)
    print(res)


"""
https://www.acwing.com/activity/content/punch_the_clock/11/
不断分块
分块后一遍排序一遍算逆序对
算完后排序那一块，使得这一块后面不会被重复计算
"""