"""
给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。

若可行，输出任意可行的结果。若不可行，返回空字符串。

示例 1:

输入: S = "aab"
输出: "aba"
示例 2:

输入: S = "aaab"
输出: ""
"""

class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        # 创建一个最大堆， 里面储存的结构式 (-元素个数,元素)， heap会按照第一个元素的大小来进行排序
        # heapq在python 中是最小堆（最小元素在堆顶）， 要把元素个数取负，这样才能构成一个以元素个数为从大到小顺序的
        # 最大堆
        maxheap = []
        for x in set(S):
            maxheap.append((-S.count(x), x))

        # 排序
        heapq.heapify(maxheap)

        # 当一个元素超过数量一半的时候，肯定无法保证它和别的元素能排不同到一起，返回空
        for count,x in maxHeap:
            # len(s) + 1//2 的目的是， 当len(s)为奇数的时候，保证它不会向下取整
            # 例如 3//2 = 1 ，（3+1）//2 = 2
            if -count > (len(S) + 1)//2:
                return ""

        res = []
        while len(maxheap) >= 2:
            count1,letter1 = heapq.heappop(maxheap)
            count2,letter2 = heapq.heappop(maxheap)

            # 把字符进行拼接
            res += [letter1,letter2]

            # 每使用完一次元素以后， count要减少1， 重新添加回heap中， 供下次使用
            if count1 + 1 != 0:
                heapq.heappush(maxheap, (count1+1, letter1))
            if count2 + 1 != 0:
                heapq.heappush(maxheap, (count2+1, letter2))

        # 最后把res给拼成字符串， 如果maxheap里还有元素的话也加进去
        return "".join(res) + (maxheap[0][1] if maxheap else "")

"""
621,767可以一起看

Time: O(NlogA) Space: O(A)
https://leetcode-cn.com/problems/reorganize-string/solution/zhong-gou-zi-fu-chuan-by-leetcode/

在堆中存储 (count, letter) 这种格式的元素（在 Python 的实现中存储的是 count 的负数形式）。
每次从堆中弹出两个元素出来（代表两个剩余次数最大和第二大的字符），接着将这两个字符中与之前输出字符不同
出现次数最大的字符输出。之后把重新计算的剩余次数和字符再压入栈中。
最后，堆中可能会剩下一个元素，这个元素出现次数一定是 1。如果不是的话，那就不可能有这种排列
"""

