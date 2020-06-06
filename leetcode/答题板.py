class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        record = [0] * len(height)

        leftmost = -1
        for i in range(len(height)):
            leftmost = max(leftmost, height[i])
            record[i] = max(record[i], leftmost)

        res = 0
        rightmost = -1
        for j in range(len(height)-1, -1, -1):
            rightmost = max(rightmost, height[i])
            res = min(rightmost, record[i])

        return res
