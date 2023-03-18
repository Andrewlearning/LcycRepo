
## 什么是DFS？Depth First Search英文的缩写。
主要思想：不撞南墙不回头。

深度优先遍历的主要思想就是：首先以一个未被访问过的顶点作为起始顶点，沿当前顶点的边走到未访问过的顶点；当没有未访问过的顶点时，则回到上一个顶点，继续试探访问别的顶点，直到所有的顶点都被访问。

沿着某条路径遍历直到末端，然后回溯，再沿着另一条进行同样的遍历，直到所有的顶点都被访问过为止。

- Backtracking is a more general purpose algorithm.
- Depth-First search is a specific form of backtracking related to searching graph, tree structures.


```
一个模板:

res = []
def backtrack(路径，选择列表):
    if 满足结束条件:
        res.append(路径)
        return
      
    for 选择 in 选择列表:
        做选择
        backtrack(路径，选择列表)
        撤销选择
```

## dfs一般使用场景
模板dfs，mask举例dfs
外部空间dfs (用stack写成iterative way, for example tree traversal)
dfs+memo (DP减枝)
使用在模拟流程，寻找所有情况全排列解

## 来源-古城算法
https://docs.google.com/presentation/d/1pU6V3tGvldbAXk_qrcNOqE85vfv9Ty-raBP2XcDacyo/edit#slide=id.g9dd079ca29_3_12