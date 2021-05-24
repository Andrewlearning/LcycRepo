"""
给定一个如下图所示的数字三角形，从顶部出发，在每一结点可以选择移动至其左下方的结点或移动至其右下方的结点，一直走到底层，要求找出一条路径，使路径上的数字的和最大。

        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5

7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""
if __name__ == "__main__":
    n = int(input())
    triangle = []

    for _ in range(n):
        line = [-float('inf')] + list(map(int, input().split())) + [-float('inf')]
        triangle.append(line)

    for i in range(1, n):
        for j in range(1, len(triangle[i])-1):
            triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    print(max(triangle[-1]))

# 思路是从是从上往下选
# 链接：https://www.acwing.com/activity/content/code/content/163999/
