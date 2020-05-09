"""
假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示
其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来实现这个队列。


输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

[5,0]前面大与或等于他身高的0个人
[7,0]前面大与或等于他身高的0个人
[5,2]前面大与或等于他身高的2个人。。。
"""

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # 先按照身高从高到矮排，然后再按照index从小到大排
        people.sort(key=lambda x: (-x[0], x[1]))
        output = []

        for p in people:
            # 按照这个人的前面身高有几个人，来插入
            output.insert(p[1], p)
        return output

"""
时间复杂度：O(N^2)
排序使用了 O(NlogN) 的时间，每个人插入到输出队列中需要 O(k) 的时间其中 k 是当前输出队列的元素个数。
 
空间复杂度：O(N)，输出队列使用的空间。

这题看题解把，真想不到
https://leetcode-cn.com/problems/queue-reconstruction-by-height/solution/gen-ju-shen-gao-zhong-jian-dui-lie-by-leetcode/

解法：
将最高的人按照 k 值升序排序，然后将它们放置到输出队列中与 k 值相等的索引位置上。
按降序取下一个高度，同样按 k 值对该身高的人升序排序，然后逐个插入到输出队列中与 k 值相等的索引位置上。
直到完成为止。


"""