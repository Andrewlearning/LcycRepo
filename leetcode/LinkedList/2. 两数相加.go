package LinkedList

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {

    head := new(ListNode)
    res := head
    carry := 0
    cur := 0
    p1 := l1
    p2 := l2

    for p1 != nil || p2 != nil || carry > 0 {
        cur = carry
        carry = 0

        if p1 != nil {
            cur += p1.Val
            p1 = p1.Next
        }

        if p2 != nil {
            cur += p2.Val
            p2 = p2.Next
        }

        if cur >= 10 {
            carry = 1
            cur -= 10
        }

        nxt := &ListNode {
            Val : cur,
        }
        head.Next = nxt
        head = nxt
    }

    return res.Next
}