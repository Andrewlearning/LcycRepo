"""
有向无环图，被称为拓扑图，一定存在一个拓扑序列
假如我们把一个图按照拓扑序排好，那么一定是从前面指向后面的

度数：
入度：一个点有多少条边指向自己
出度：一个点有多少条边出去

所有入度为0的点都可以作为拓扑排序排最前面的点

queue <- 所有入度为0的点
while queue:
    tt = queue.popleft()
    枚举tt的所有出边:
        删除tt -> 下一个点的边 d[j]--
        if d[j] == 0:
            queue <- j

一个有向无环图一定至少存在一个入度为0的点
"""