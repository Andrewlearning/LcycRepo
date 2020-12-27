/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseKGroup(head *ListNode, k int) *ListNode {

    tail := head
    for i := 0; i < k; i++ {
        if tail == nil {return head}
        tail = tail.Next
    }


    newHead := reverse(head, tail)
    head.Next = reverseKGroup(tail, k)

    return newHead


}


func reverse(head *ListNode, tail *ListNode) *ListNode {
    var pre *ListNode = nil
    cur := head

    for cur != tail {
        next := cur.Next
        cur.Next = pre

        pre = cur
        cur = next
    }

    return pre

}