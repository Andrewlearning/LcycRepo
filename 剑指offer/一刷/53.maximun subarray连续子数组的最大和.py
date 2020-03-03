

class Solution:
    #1
    def FindGreatestSumOfSubArray(self, array):
        cursum = maxsum = array[0]
        for num in array[1:]:
            cursum = max(cursum, cursum + num)
            maxsum = max(cursum, maxsum)
        return maxsum

    #2
    def maxSubArray(self, array):
        """
        :type nums: List[int]
        :rtype: int
        """
        cursum = maxsum = array[0]
        for num in array[1:]:
#假如说你的cursum已经小于0了，那么不如从下一位非0的重新开始,因为next 绝对大于 next + cursum
            if cursum <= 0:
                cursum = num
            else:
                cursum += num

            if cursum > maxsum:
                maxsum = cursum
        return maxsum

if __name__ == "__main__":
    solution = Solution()


"""
https://algocasts.io/episodes/deG4vW1R
Time: O(n), Space: O(1)
对应leetcode 53.maximun subarray
原理非常简单暴力，关键在 cursum = max(i, cursum + i)，看看加上
下一个数是不是与 直接用下一个数 ，哪个比较大

1.有客观规律就是，假如说你的cursum已经小于0了，那么不如从下一位非0的重新开始
因为next 绝对大于 next + cursum

"""