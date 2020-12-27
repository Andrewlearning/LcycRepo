def binarySearch(array, target):

    # 左闭右闭区间
    l, r = 0, n - 1
    # 左边界
    while l < r:
        mid = (l + r) // 2
        # [l, mid] [mid+1, r]
        if array[mid] < target:
            l = mid + 1
        else:
            r = mid

    if array[l] != target:
        return ["-1", "-1"]
    res1 = l

    l, r = 0, n - 1
    # 右边界
    while l < r:
        mid = (l + r + 1) // 2
        # [l, mid-1] [mid, r]
        if array[mid] <= target:
            l = mid
        else:
            r = mid - 1

    return [str(res1), str(l)]


if __name__ == "__main__":
    n, q = map(int, input().split())
    array = list(map(int, input().split()))
    query = []
    for _ in range(q):
        query.append(int(input()))

    res = ""
    for target in query:
        res += " ".join(binarySearch(array, target)) + '\n'
    print(res.rstrip())

"""
思路：https://www.acwing.com/video/231/
代码：https://www.acwing.com/activity/content/code/content/255271/
"""