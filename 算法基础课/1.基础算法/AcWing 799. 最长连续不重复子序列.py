"""

双指针算法是将
for i in range(n):
    for j in range(n):

从O(n^2)优化为O(n)

for (i = 0; j = 0; i < n; i++) {
    while (j < i && check(i,j)) j++;

    每道题目的具体逻辑
}

"""
def main(nums, n):
    hashmap = [0] * 100001
    res = 0

    j = 0
    for i in range(len(nums)):
        hashmap[nums[i]] += 1

        while hashmap[nums[i]] > 1:
            hashmap[nums[j]] -= 1
            j += 1

        res = max(res, i - j + 1)

    return res


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))

    print(main(nums, n))

# https://www.acwing.com/video/245/