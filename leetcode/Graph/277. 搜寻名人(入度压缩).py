"""
输入: graph = [
  [1,1,0],
  [0,1,0],
  [1,1,1]
]
输出: 1
解析: 有编号分别为 0、1 和 2 的三个人。graph[i][j] = 1 代表编号为 i 的人认识编号为 j 的人，而 graph[i][j] = 0 则代表编号为 i 的人不认识编号为 j 的人。“名人” 是编号 1 的人，因为 0 和 2 均认识他/她，但 1 不认识任何人。
"""


# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
def knows(a, b):
    pass
class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 我们先初始化候选人为第一个人
        candidate = 0

        # 观察图可知，每个节点，最多只有一个箭头
        # 另一个规律是，假如说有一个名人，那么所有的箭头都指向他
        # 所以，假如说真有一个名人，那么我们任意找到一个箭头的指向，都会指向那个名人
        for j in range(1, n):
            # 假如 candidate认识j, 说明j有可能是名人
            if knows(candidate, j):
                candidate = j

        # 判断是否符合条件
        for j in range(n):
            # 名人只认识自己，跳过
            if candidate == j:
                continue
            # 假如发现名人还认识别人，说明它不是名人
            if knows(candidate, j):
                return -1
            # 假如别人不认识名人，说明它不是名人
            if not knows(j, candidate):
                return -1

        return candidate

# 链接：https://leetcode-cn.com/problems/find-the-celebrity/solution/c-shuang-100jian-dan-ti-jie-by-da-li-wang/
