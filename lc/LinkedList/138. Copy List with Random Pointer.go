/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

func copyRandomList(head *Node) *Node {

    m := make(map[*Node]*Node)

    cur := head
    for cur != nil {
        m[cur] = &Node{Val:cur.Val}
        cur = cur.Next
    }

    cur = head
    for cur != nil {
        if cur.Next != nil {
            m[cur].Next = m[cur.Next]
        }
        if cur.Random != nil {
            m[cur].Random = m[cur.Random]
        }
        cur = cur.Next
    }

    return m[head]
}