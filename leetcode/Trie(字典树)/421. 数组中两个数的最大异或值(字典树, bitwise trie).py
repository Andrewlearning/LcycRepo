"""
给定一个非空数组，数组中元素为 a0, a1, a2, … , an-1，其中 0 ≤ ai < 231。
找到 ai 和aj最大的异或 (XOR) 运算结果，其中0 ≤ i,j < n。
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

        trie = {}
        for num in nums:
            node = trie
            # 为什么要倒着遍历，因为在2进制中，越左的位数则越大
            # 而我们后面进行选择XOR最大的数的时候，需要从大的位数先开始判断，然后再到小的位数，这样来进行选择
            # 例如 100 = 4, 010 = 2, 001 = 1
            for i in range(31, -1, -1):
                # num 从左往右数第i位 二进制位 是0还是1
                curBit = (num >> i) & 1

                # 以当前bit的数字(0/1)创建新的节点，然后进入这个新节点，进入下一次循环
                # 数从上往下是对应二进制的从左到右
                if curBit not in node:
                    node[curBit] = {}
                node = node[curBit]

        res = float("-inf")
        for num in nums:
            node = trie
            temp = 0
            # 从左往右对比当前num的二进制
            for i in range(31, -1, -1):
                # num 从左往右数第i位 二进制位 是0还是1
                curBit = (num >> i) & 1
                
                # num 从左往右数第i位 二进制位 潜在的最好xor位数
                # 0 ^ 1 = 1 , 1 ^ 1 = 0, 所以curBit ^ 1是看tree里面存不存在所以curBit的相反数
                # 假如存在，那么说明，当前curBit ^ bestChoise 可以得到在当前从左往右第i位的最大值
                bestChoise = curBit ^ 1

                # 因为我们要确保这个最优解的存在，所以trie就是用来走这个最优解的选项
                if bestChoise in node:
                    # 假如当前最佳选择存在，那么则把当前二级制位为1的结果加到temp中
                    temp += (1 << i)
                    node = node[bestChoise]
                # 假如不存在，那我们跳过当前这一位，进入下一位
                else:
                    node = node[curBit]

            res = max(res, temp)

        return res

# 代码 https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array/solution/qian-zhui-shu-by-powcai/
# 思路 https://www.youtube.com/watch?v=qU3SbJHb7o8&t=960s
