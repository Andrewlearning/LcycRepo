if __name__ == "__main__":

    n = int(input())

    nums = list(map(int, input().split()))

    dp = [1] * len(nums)

    res = -float("inf")

    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
                res = max(res, dp[i])

    print(res)

# lc300

def searchInsert(nums, length, target):
    l = 0
    r = length

    while l < r:
        mid = (l + r) // 2

        if nums[mid] >= target:
            r = mid
        else:
            l = mid + 1

    return l


def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums is None:
        return []

    n = len(nums)
    res = [0] * n
    reslen = 0

    for x in nums:
        i = searchInsert(res, reslen, x)
        # 更新结果子串
        res[i] = x
        if i == reslen:
            reslen += 1
    return reslen


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(lengthOfLIS(nums))
