"""
给定一个浮点数n，求它的三次方根。

输入格式
共一行，包含一个浮点数n。

输出格式
共一行，包含一个浮点数，表示问题的解。

注意，结果保留6位小数。

数据范围
−10000≤n≤10000

"""
def binarySearch(target):
    l = -10000
    r = 10000
    # 1的-8次方
    # 0后有6位小数，留1的-8次方比较好
    threshold = 1e-8

    while r - l > threshold:
        mid = (l + r) / 2
        if mid ** 3 < target:
            l = mid
        else:
            r = mid

    return '{0:.6f}'.format(l)


if __name__ == "__main__":
    n = float(input())
    print(binarySearch(n))

"""
思路：https://www.acwing.com/video/232/
代码：https://www.acwing.com/activity/content/code/content/153766/
"""