/**

给定一个链表，删除链表的倒数第n个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
 */

package LinkedList

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {

	dummy := new(ListNode)
	dummy.Next = head
	fast := dummy

	for fast != nil && n > 0 {
		fast = fast.Next
		n -= 1
	}


	slow := dummy
	slowslow := dummy
	for fast != nil {
		slowslow = slow
		slow = slow.Next
		fast = fast.Next
	}

	slowslow.Next = slow.Next

	return dummy.Next

}