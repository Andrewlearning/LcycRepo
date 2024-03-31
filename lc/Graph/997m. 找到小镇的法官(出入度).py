"""
在一个小镇里，按从 1 到 N 标记了 N 个人。传言称，这些人中有一个是小镇上的秘密法官。

如果小镇的法官真的存在，那么：

小镇的法官不相信任何人。
每个人（除了小镇法官外）都信任小镇的法官。
只有一个人同时满足属性 1 和属性 2 。
给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示标记为 a 的人信任标记为 b 的人。

如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的标记。否则，返回 -1。

"""
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        inDegree = [0] * (N + 1)
        outDegree = [0] * (N + 1)

        for frm, to in trust:
            inDegree[to] += 1
            outDegree[frm] -= 1

        for i in range(1, len(inDegree)):
            # 法官是除他以外所有人(N-1)都指向他
            # 且法官不指向任何人
            if inDegree[i] == N - 1 and outDegree[i] == 0:
                return i

        return -1