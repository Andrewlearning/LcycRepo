class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        # 表示，有多少个元素的时候，最少的分割次数，所以是[0,len]
        # 0个元素无法被分割，最多被分割-1次
        # 1个元素的时候最多能被分割0次
        # 两个元素的时候，最多能被分割1次
        cut = [i - 1 for i in range(len(s) + 1)]

        for i in range(len(s)):
            self.expend(s, i, i, cut)
            self.expend(s, i, i + 1, cut)

        return cut[-1]

    def expend(self, s, l, r, cut):
        # 当l == r时，可以扩散
        # 那么r + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            # 因为我们把cur[r+1]变为最少的扩散次数
            # 所以我们要不断把 cut[l] + 回文串，向左推
            cut[r + 1] = min(cut[r + 1], cut[l] + 1)
            l -= 1
            r += 1


"""
Time: O(n^2), Space: O(n)
https://algocasts.io/episodes/k8GN2lGe

"""