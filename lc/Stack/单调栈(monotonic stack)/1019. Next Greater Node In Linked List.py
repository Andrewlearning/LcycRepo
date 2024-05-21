"""
You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next greater node.
That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed).
If the ith node does not have a next greater node, set answer[i] = 0.

Input: head = [2,1,5]
Output: [5,5,0]

Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]
"""
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # 遍历整个链表，把每个节点的值都记录下来
        nums = []
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next

        # 后面就是熟悉的单调栈模板，可以参考496
        n = len(nums)
        stack = []
        nextLarger = [0] * n

        for i in range(n - 1, -1, -1):
            x = nums[i]

            while stack and x >= stack[-1]:
                stack.pop()

            if stack:
                nextLarger[i] = stack[-1]

            stack.append(x)

        return nextLarger

# acwing https://www.acwing.com/video/3560/