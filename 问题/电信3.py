import sys


def q3(nums):
    if len(nums) <= 2:
        return max(nums)

    dp = [0 for i in range(len(nums))]
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    return dp[-1]



if __name__ == "__main__":
    data =[]
    while True:
        line = sys.stdin.readline().strip().split()
        if not line:
            break
        line = map(int, line.split())
        data.append(line)

    print(data)

    values = map(int, line.split(","))



    print(q3(values))

