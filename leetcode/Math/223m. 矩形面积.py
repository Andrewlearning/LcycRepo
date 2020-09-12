class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # 我们以abcd作为中心矩形，efgh来判断是否有重叠部分
        if G <= A or H <= B or E >= C or D <= F:
            return (C - A) * (D - B) + (G - E) * (H - F)

        # 假如有重叠部分，我们找出上下左右四个角的最内聚部分，他们的乘积就是重叠部分
        up = min(D, H)
        down = max(B, F)
        left = max(A, E)
        right = min(C, G)

        total = (C - A) * (D - B) + (G - E) * (H - F)
        same = (up - down) * (right - left)

        return total - same


# https://leetcode-cn.com/problems/rectangle-area/solution/jian-dan-de-kao-lu-by-powcai/