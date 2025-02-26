/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseBetween(head *ListNode, left int, right int) *ListNode {

    dummy := &ListNode{Next:head}
    edge := dummy

    for i := 0; i < left - 1; i++ {
        edge = edge.Next
    }

    pre := edge.Next
    cur := pre.Next
    for i := 0; i < right - left; i++ {
        nxt := cur.Next

        cur.Next = pre
        pre = cur
        cur = nxt
    }

    edge.Next.Next = cur
    edge.Next = pre
    return dummy.Next
}