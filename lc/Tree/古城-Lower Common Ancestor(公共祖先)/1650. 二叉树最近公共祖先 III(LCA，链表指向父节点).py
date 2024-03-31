"""
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
"""
class Solution:
    def lowestCommonAncestor(self, p, q):
        s = set()
        while p:
            s.add(p)
            p = p.parent

        while q:
            if q in s:
                return q
            q = q.parent


