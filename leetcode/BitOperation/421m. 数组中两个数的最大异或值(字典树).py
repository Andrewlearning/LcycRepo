"""
给定一个非空数组，数组中元素为 a0, a1, a2, … , an-1，其中 0 ≤ ai < 231 。
找到 ai 和aj 最大的异或 (XOR) 运算结果，其中0 ≤ i,  j < n 。
你能在O(n)的时间解决这个问题吗？
示例:
输入: [3, 10, 5, 25, 2, 8]
输出: 28
解释: 最大的结果是 5 ^ 25 = 28.
"""
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums and len(nums) == 0:
            return 0

        root = {}
        for num in nums:
            tree = root
            for i in range(31, -1, -1):
                # 看当前bit是0还是1
                cur_bit = (num >> i) & 1
                # 以当前bit的数字创建新的节点，然后进入这个新节点，进入下一次循环
                tree.setdefault(cur_bit, {})
                tree = tree[cur_bit]

        res = float("-inf")
        for num in nums:
            tree = root
            temp = 0
            for i in range(31, -1, -1):
                cur_bit = (num >> i) & 1
                # 0 ^ 1 = 1 , 1 ^ 1 = 0, 所以cur_bit ^ 1是看tree里面存不存在相反数
                # 假如存在，那么说明，当前位进行异或^的话可以得到一个最大值
                if cur_bit ^ 1 in tree:
                    temp += (1 << i)
                    # 加完当前位以后，我们进入下一位
                    tree = tree[cur_bit ^ 1]
                # 假如不存在，那我们跳过当前这一位，进入下一位
                else:
                    tree = tree[cur_bit]

            res = max(res, temp)

        return res

# 代码 https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array/solution/qian-zhui-shu-by-powcai/
# 思路 https://www.acwing.com/video/1827/
