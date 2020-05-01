class Solution:
    def grayCode(self, n):
        res, head = [0], 1
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(head + res[j])
            head <<= 1
        print(res)
        return res

s = Solution()
s.grayCode(2)
"""
https://leetcode-cn.com/problems/gray-code/solution/gray-code-jing-xiang-fan-she-fa-by-jyd/

"""
