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
		if tail == nil {
			return head
		}
		tail = tail.Next
	}
	/*
	   head = [1,2,3,4,5], k = 2
	   reverse(1,3) → 翻转 1->2 变为 1(head)<-2(newHead)
	   1.Next = reverseKGroup(3,2)
	   reverse(3,5) → 翻转 3->4 变为 3(head)<-4(newHead)
	   3.Next = reverseKGroup(5,2) 递归处理 5
	   tail 走 2 步，但 tail == nil，说明 不足 k=2 个, 直接返回 5
	   最终2(newHead)->1(head)->4(newHead)->3(head)->5
	*/
	newHead := reverse(head, tail)
	head.Next = reverseKGroup(tail, k)

    // 因为翻转后变为 // newHead -> xx -> head -> 
	return newHead

}

// 与206一样
func reverse(head *ListNode, tail *ListNode) *ListNode {
	var pre *ListNode
	cur := head

	for cur != tail {
		next := cur.Next
		cur.Next = pre

		pre = cur
		cur = next
	}

	return pre

}

/*
时间复杂度： O(n)，每个节点最多访问两次（一次遍历 tail，一次翻转）。
空间复杂度： O(n/k)，由于递归调用栈的深度是 n/k。
*/
