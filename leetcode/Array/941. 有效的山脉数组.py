class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if not A or len(A) == 0:
            return

        # 一开始向上走
        p = 0
        # 这里的一个处理是p + 1 < len(A)， 然后后续p,p+1比较，这样就能保证所有数字都能被比较到，且不会越界了
        # 这里和 dp子串小总结里的处理情况有点不一样，可以注意一下，因为这里是单个数组，dp里是dp一个数组，array一个数组
        while p + 1 < len(A) and A[p] < A[p + 1]:
            p += 1

        # 山顶不能在一开始或者是最后
        if p == 0 or p + 1 == len(A):
            return False

        # 然后再往下走
        while p + 1 < len(A) and A[p] > A[p + 1]:
            p += 1

        # 向下走走到底以后，看看是否走到了最后，走到最后的话说明确实是呈现一个山脉的状态
        return p + 1 == len(A)

"""
Time: O(n) Space:O(1)
https://leetcode-cn.com/problems/valid-mountain-array/solution/you-xiao-de-shan-mai-shu-zu-by-leetcode/
"""