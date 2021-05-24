"""
输入格式
共一行，包含一个整数n。

输出格式
按字典序输出所有排列方案，每个方案占一行。

数据范围
1≤n≤7
输入样例：
3
输出样例：
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""

def dfs():
    if len(temp) == n:
        res.append(temp[:])
        return

    for i in range(1, n + 1):
        if i not in memo:
            temp.append(i)
            memo.append(i)
            dfs()
            memo.pop(-1)
            temp.pop(-1)


if __name__ == "__main__":

    n = int(input())
    temp = []
    res = []
    memo = []
    dfs()
    for item in res:
        print(" ".join(map(str, item)))

