import sys
# “C a b”，在点a和点b之间连一条边
# 这里是x->y
def merge(x, y):
    # 假如这两个节点是同一个节点，那么就不要进行后面size的修改了
    if find(x) == find(y):
        return
        # 这里先加后连，逻辑错了的话会重复机选
    size[find(y)] += size[find(x)]
    uf[find(x)] = find(y)


# “Q1 a b”，询问点a和点b是否在同一个连通块中
def find(x):
    if uf[x] != x:
        uf[x] = find(uf[x])
    return uf[x]


if __name__ == "__main__":
    n, m = map(int, input().split())

    uf = [i for i in range(n + 1)]
    size = [1] * (n + 1)

    for i in range(m):
        # 这里用input.split会超时
        line = list(sys.stdin.readline().strip().split())
        op = line[0]
        nums = list(map(int, line[1:]))

        if op == "C":
            merge(nums[0], nums[1])

        elif op == "Q1":
            if find(nums[0]) == find(nums[1]):
                print("Yes")
            else:
                print("No")
        # 只返回最高节点的值
        elif op == "Q2":
            print(size[find(nums[0])])


