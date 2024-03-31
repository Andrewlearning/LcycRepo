"""
Assume you have an array of length n initialized with all 0's and are given k update operations.
Each operation is represented as a triplet:
[startIndex, endIndex, inc] which increments each element of
subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.
Return the modified array after all k operations were executed.

Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]
"""

class Solution(object):
    def getModifiedArray(self, length, updates):
        res = [0] * length
        for update in updates:
            value = update[2]
            start = update[0]
            end = update[1]

            # 把区间的第一个元素 + value
            res[start] += value

            # 假如end还在列表内，则区间最后一个元素 - value
            if end < length - 1:
                res[end + 1] -= value

        # 记录前面所有加减到当前位置的值
        curSum = 0
        for i in range(length):
            curSum += res[i]

            # 这是本题关键，由于我们在区间开始部分已经+value了
            # 那么这个修改会一直赋值给区间内的所有位置
            # 出区间的时候-value, 使得不会影响到其他元素
            res[i] = curSum

        return res

"""
这题技巧性比较强，这个叫lazy propagation
古城算法 33:00
https://www.bilibili.com/video/BV1xB4y1N7Ut/?spm_id_from=333.337.search-card.all.click&vd_source=b81616a45fd239becaebfee25e0dbd35

[1,3,2] [2,3,3] length=5
res = [0,2,0,0,-2]
res = [0,2,3,0,-5]
sum = [0,2,5,5,0]
res = [0,2,5,5,0]
"""
