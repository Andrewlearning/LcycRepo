"""
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array.
Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once.
 Formally, for a subarray nums[i], nums[i + 1], ..., nums[j],
 there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
"""


def maxSubarraySumCircular(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 局部最大序列和
    curMax = 0
    # 全局最大序列和
    maxSum = nums[0]

    # 局部最小序列和
    curMin = 0
    # 全局最小序列和
    minSum = nums[0]

    # nums所有元素的和
    total = 0

    for num in nums:
        curMax = max(curMax + num, num)
        maxSum = max(maxSum, curMax)

        curMin = min(curMin + num, num)
        minSum = min(minSum, curMin)

        total += num

    # 当nums全部为负数的时，total - minSum = 0，所以max(maxSum, total - minSum)=0
    # 但真实结果应该为maxSum
    if maxSum < 0:
        return maxSum
    # 在case1和case2两个答案中取最优
    return max(maxSum, total - minSum)

"""
参考自 https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/One-Pass

例如 [5,-3, 5], 我们可以把它想象成存在 [5,-3, 5 | 5,-3, 5]
case1: 最大子数组没有跨越边界
例如: [-4,1,2,-5], 最大子数组是[1,2]

case2: 最大子数组需要跨越边界
例如: [5,-3,5] -> [5,-3,(5,5),-3,5] -> 最大子数组是[5,5]
其实[5,-3,(5,5),-3,5] 相当于是 total[5,-3,5] - minSum[-3] = [5,5]
所以应对case2, 我们只需要求出 数组的和 - 最小子数组 = 最大子数组

所以综合上面case1, case2
res = max(maxSum, total - minSum)

corner case:
假如存在一个数组是全部都是负数，例如[-1,-2,-3]
那么maxSum=-1, total(-6) - minSum(-6) = 0, max(maxSum, total - minSum) = 0
0并不符合我们的要求
所以在这种情况下，假如maxSum < 0, 则返回maxSum的值


关于Kadane's Algotithm
https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
下面是伪代码的python implement

def GFG(a, size):
    # 全局序列和最大值
    max_so_far = float('-inf')  
    
    # 当前序列和最大值
    max_ending_here = 0
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        # 假如当前序列和最大值 优于 全局最大值，则更新全局最大值
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        # 假如当前序列和 < 0，则抛弃这个答案，重新开始极速
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far
"""
