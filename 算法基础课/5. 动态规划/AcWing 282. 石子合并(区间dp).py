"""
设有N堆石子排成一排，其编号为1，2，3，…，N。

每堆石子有一定的质量，可以用一个整数来描述，现在要将这N堆石子合并成为一堆。

每次只能合并相邻的两堆，合并的代价为这两堆石子的质量之和
合并后与这两堆石子相邻的石子将和新堆相邻，合并时由于选择的顺序不同，合并的总代价也不相同。

输入样例：
4
1 3 5 2
输出样例：
22
"""
if __name__ == "__main__":

    n = int(input())
    nums = [0] + list(map(int, input().split()))

    # dp[i][j] 从i~j这个范围以内的石头合并最少的次数是多少
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # 求前缀和
    prefixSum = [0] * len(nums)
    for i in range(1, len(prefixSum)):
        prefixSum[i] = nums[i] + prefixSum[i - 1]

    # 区间长度,区间长度为1的时候说明石头不需要合并，跳过了
    for len in range(2, n + 1):
        # 这个层循环是定义左区间的位置
        for i in range(1, n - len + 2):
            # while l + len - 1 <= n -> l <= n - len -1
            l = i
            r = i + len - 1
            dp[l][r] = float("inf")
            # 定义k定义分界线
            for k in range(l, r):
                # 每次两堆石头合并，要进行prefixSum[r] - prefixSum[l-1]次操作
                dp[l][r] = min(dp[l][r], dp[l][k] + dp[k + 1][r] + (prefixSum[r] - prefixSum[l - 1]))

    print(dp[1][n])


# https://www.acwing.com/video/943/

