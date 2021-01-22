"""
离散化特征：值域跨度很大，但是很稀疏
应用场景：
我们要做的就是，把这些数，都原来下标重新映射到一个数组，这样的话，中间很多不存在的数，就不用去计算了


有一个数组，值域[0 ~ 10**9], 有10**5个元素
例如：
a[] = 1,3,100,2000,50000
i   = 0,1,2,  3,   4

离散化的前提
1.a中可能有重复元素，对a进行去重
2.如何算出x离散化后的值, 二分

"""

n, m = map(int, input().split())

# 二维数字[下标，要加的数]
addNum = []
# 二维数组, 需要被query的[左下标，右下标]
query = []
# 这个离散化数组所拥有的下标
indexList = []


for i in range(n):
    x, c = map(int, input().split())
    addNum.append([x, c])
    indexList.append(x)

for i in range(m):
    l, r = map(int, input().split())
    query.append([l, r])
    indexList.append(l)
    indexList.append(r)

# 离散化操作
indexList.sort()
indexList = list(set(indexList))

# 在离散化数组里进行二分查找(这个模板是找左边界，但实际上找单个也可以)
def find(x):
    l = 0
    r = len(indexList) - 1
    while l < r:
        mid = (l + r) >> 1
        if x <= indexList[mid]:
            r = mid
        else:
            l = mid + 1
    return r + 1  # 离散化后的序号为1 ~ len(indexList)-1


# 注意nums序号从1到len-1
# prefixSum[0]=0 prefixSum[1] = nums[1]
nums = [0] * (len(indexList) + 1)
prefixSum = [0] * (len(indexList) + 1)

# 给对应位置的元素 +c
for x, c in addNum:
    nums[find(x)] += c

# 求前缀和，方便后面算query
for i in range(1, len(indexList) + 1):
    prefixSum[i] = prefixSum[i - 1] + nums[i]

# 利用前缀和算query范围内的值
for i in query:
    l, r = find(i[0]), find(i[1])
    print(prefixSum[r] - prefixSum[l - 1])

# 思路：https://www.acwing.com/video/247/
# 代码：https://www.acwing.com/activity/content/code/content/487731/
