## Dijikstra Algorithm 
### A single source shotest path Algotithm
### 单源头最短路径算法


## Dijikstra核心思想
- 我们从起点u作为中心慢慢的向四周扩散，同时我们不断更新到达其他点的最短距离。
- Dijikstra是一个贪心算法，每一步选择的都是从当前已经到达点出发，到没有visited过点的最小权重的edge，这样来找到达其他点的最短路径。

## Dijikstra的算法局限
- 在负weighted edge的情况下，贪心无法选择最后结果最短的边

## Dijikstra的适用情况
- Dijkstra算法可以解决无负权图的最短路径问题，只能应付单源起点的情况，算法要求两个集合，开始所有点在第二个集合，然后将起点加入第一个集合，接着第二个集合剩下的点哪个离起点距离最小，就加入第一个集合，并对其相关的边进行松弛，如此循环直到所有点都进入集合。
- 每个点都加进集合需要循环n次，每个点进入集合又要对不在集合的点距离进行更新，内层又要循环n次。开始将map全部初始化为INF（一个很大的数），这样松弛的时候比较轻松

### source
- 古城算法 图的基础算法(五) -- Dijkstra 精讲 https://www.bilibili.com/video/BV1K44y1v7wp