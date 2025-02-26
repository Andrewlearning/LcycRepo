/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    carry := 0
    res := &ListNode{}
    head := res

    for carry != 0 || l1 != nil || l2 != nil {
        cur := carry
        carry = 0
        if l1 != nil {
            cur += l1.Val
            l1 = l1.Next
        }
        if l2 != nil {
            cur += l2.Val
            l2 = l2.Next
        }

        if cur >= 10 {
            cur -= 10
            carry = 1
        }

        head.Next = &ListNode{Val:cur}
        head = head.Next
    }
    return res.Next
}