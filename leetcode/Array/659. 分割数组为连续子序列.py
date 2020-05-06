"""
输入一个按升序排序的整数数组（可能包含重复数字
你需要将它们分割成几个子序列，其中每个子序列至少包含三个连续整数。
返回你是否能做出这样的分割？
"""
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # count[x]：存储原数组中数字i出现的次数
        # tail[x]：存储以数字x结尾的且符合题意的连续子序列个数
        count = collections.Counter(nums)
        tails = collections.Counter()

        for x in nums:
            # 数量为0，无法操作，跳过
            if count[x] == 0:
                continue

            # 如果后续发现有能够接在这个连续子序列的数字x+3
            # 则延长以x+2为结尾的连续子序列到x+3
            # 此时消耗nc[x+3]一个，由于子序列已延长，因此tail[x+2]减1，tail[x+3]加1
            elif count[x] > 0 and tails[x-1] > 0:
                count[x] -= 1
                tails[x - 1] -= 1
                tails[x] += 1

            # 先去寻找一个长度为3的连续子序列x, x+1, x+2
            # 找到后就将count[x], count[x+1], count[x+2]中对应数字消耗1个（即-1）
            # 并将tail[x+2]加1，即以x+2结尾的子序列个数+1。
            elif count[x] > 0 and count[x + 1] > 0 and count[x + 2] > 0:
                count[x   ]  -= 1
                count[x + 1] -= 1
                count[x + 2] -= 1
                tails[x + 2] += 1

            # 如果count[x]不为0，说明这个数字多出来了，且无法组成连续子序列
            # 所以可以直接返回false了
            else:
                return False

        return True

"""
时间复杂度：O(N)，所有元素遍历一遍O(N)，循环内部均为常数时间操作O(1)
空间复杂度：O(N)，使用了两个哈希map

https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences/solution/tan-xin-suan-fa-jian-cha-shu-zu-neng-fou-bei-fen-w/
"""