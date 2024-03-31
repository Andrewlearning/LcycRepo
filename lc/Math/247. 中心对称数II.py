"""
中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。

找到所有长度为 n 的中心对称数。

示例 :

输入:  n = 2
输出: ["11","69","88","96"]

输入:  n = 3
输出: ["101","609","808","906","111","619","818","916","181","689","888","986"]
不存在 010 这种0 在外圈的组合
"""

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.helper(n, True)

    def helper(self, n, first=False):
        # 递归的终止条件
        if n == 0:
            return ['']
        if n == 1:
            return ['0', '1', '8']

        res = []

        for center in self.helper(n - 2):
            # 我们不能把0 放到最外圈
            if not first:
                res.append('0' + center + '0')
            res.append('1' + center + '1')
            res.append('6' + center + '9')
            res.append('8' + center + '8')
            res.append('9' + center + '6')
        return res

"""
Time: O(n)
Space: O(N)

这题的逻辑是:
1。 内圈，我们可以不考虑是单数还是双数的，可以放 0，1，8，因为这几个数无论怎么上下颠倒都是一样的
2.  对于外圈
    2.1 我们不能把0 放到最外圈
    2.2 我们能把什么东西放在最外圈，除了11，88是百搭以外，我们还可以放69 和 96,因为他们上下颠倒起来是一样的
    
    
"""