"""
root = [1, 2, 3], k = 5
输出: [[1],[2],[3],[],[]]
解释:
输入输出各部分都应该是链表，而不是数组。

示例 2：

输入:
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
输出: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
"""


class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        # 我们创造一个空间为k 的数组， 用来盛放答案
        res = [None for _ in range(k)]

        # 首先求出链表的总长度
        total_length = 0
        count = root
        while count != None:
            count = count.next
            total_length += 1

        # 求出每一个答案分段的长度
        length = total_length // k

        # 然后再求出要补充多少个1在分段答案里面
        rest = total_length % k

        # pre是作为一个答案分段的终止节点
        pre, head = None, root

        # 已知我们要创造 k个答案分段
        for i in range(k):

            # 我们把头结点放在res里
            res[i] = head

            # 这里就是当前答案分段要放多少个元素
            for j in range(length + (rest >= 1)):
                pre, head = head, head.next

                # 如果pre还存在的话，说明还没遍历到最后的一个节点，那么作为一段答案
                # 的结尾，我们应该把链表指针给 指向空
            if pre:
                pre.next = None

            rest -= 1

        return res

"""
https://www.bilibili.com/video/BV1KW411S7ti?from=search&seid=659522802789565863
"""