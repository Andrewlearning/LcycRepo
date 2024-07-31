"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0

        # n个节点所能构成的二叉树的数量
        dp = [0] * (n + 1)

        # 当子树节点个数为0时，代表只有一种排列情况
        dp[0] = 1

        # 当子树节点个数为1时，也代表只有一种排列情况
        dp[1] = 1

        # 在存在i个节点时
        for i in range(2, n + 1):
            # 我们用j作为root节点
            # 左子树，由比j小的元素构成，已知比j小的共有j-1个元素
            # 右子树，由比j大的元素构成，已知比j大的有i-j个元素
            for j in range(1, i + 1):
                # i所有能构成树的情况， 等于左右子树的所有可能性相乘
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[n]

# https://leetcode-cn.com/problems/unique-binary-search-trees/solution/hua-jie-suan-fa-96-bu-tong-de-er-cha-sou-suo-shu-b/


"""
有更好的解法，直接利用数学，就不了解了
Time: O(n^2), Space: O(n)
https://algocasts.io/episodes/XZWv3Nm7
答案：
这题答案略微复杂
1.
我们用d(i）表示当有i个节点时最多能生成多少种BST
假如说我们有1，2，3三个节点
以1为root,那么root有两个右节点，所以 d(0) * d(2)
以2为root,那么root左右各一个节点，所以 d(1) * d(1)
以3为root,那么root有左边有两个节点，所以 d(2) * d(0)
2.
我们定i为当前共有i个节点，j为分配节点的数量，可以得到
d(i) =sum[i from 1 to n (d(i-1) * d(n-i))]
n = 3
d(3) = i = 1 :d(1-1) * d(3-1) -> d(0) * d(2)
       i = 2 :d(2-1) * d(3-2) -> d(1) * d(1)
       i = 3 :d(3-1) * d(3-3) -> d(2) * d(0)

注意：
1.因为我们要求的是n的数，所以得有res[n],所以需要构造长为n+1的数组
2.0个node的情况我们就不求了，但是当一遍为0个node,且有root,就默认它为1
所以dp[0],dp[1]都是为1
3.i 要遍历到n，所以range(n+1)
4.j 要遍历到i，所以range(j+1)

"""

