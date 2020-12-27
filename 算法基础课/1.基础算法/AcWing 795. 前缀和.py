def preFixSum(array, l, r):
    return prefix[r] - prefix[l - 1]


if __name__ == "__main__":
    n, q = map(int, input().split())
    array = [0] + list(map(int, input().split()))
    query = []
    for _ in range(q):
        query.append(list(map(int, input().split())))

    # index = 0前面，得再放一个0，代表前缀和为0
    prefix = [0] * len(array)
    for i in range(1, len(array)):
        prefix[i] += prefix[i - 1] + array[i]

    for l, r in query:
        print(preFixSum(prefix, l, r))