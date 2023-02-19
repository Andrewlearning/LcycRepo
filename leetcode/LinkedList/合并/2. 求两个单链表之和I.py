"""
Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
这题其实比较简单简单，不用考虑太多，因为链表是倒序相加，例如2-3-1 对应实际数字是132
所以我们从头往后加，同时考虑进位就可以了
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        phead1 = l1
        phead2 = l2
        temp, carry = 0, 0,
        res = ListNode(0)
        p = res

        # 假如这三个数一直都没有结束， 那我们就一直要往下加节点
        while phead1 or phead2 or carry:
            temp = carry
            carry = 0

            if phead1:
                temp += phead1.val
                phead1 = phead1.next
            if phead2:
                temp += phead2.val
                phead2 = phead2.next

            if temp >= 10:
                temp = temp % 10
                carry = 1

            p.next = ListNode(temp)
            p = p.next


        return res.next

"""
1
https://algocasts.io/episodes/JNmDRpOZ
Time: O(max(m, n)), Space: O(max(m, n))
答案:
1.主要要知道怎么操作carry（进位）,temp>=10时我们有进位
于此同时把carry = 1(因为两个相加最大不超过20),然后在下一次循环开始再temp = carry,carry = 0
2.一些链表的操作，p.next = ListNode(sum)
3.最后出来的时候，有可能是[5],[5],最后出来时carry = 1,所以我们还需要进一位
"""