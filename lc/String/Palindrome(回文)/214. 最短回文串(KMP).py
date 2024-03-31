"""
Given a string s, you are allowed to convert it to a palindrome
by adding characters in front of it.
Find and return the shortest palindrome you can find by performing this transformation.
在原有的字符串上加点 新char,使整个字符串变成一个回文字符串
Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"
"""

class Solution(object):
    # abab [0,0,1,2] ab = ab
    # abcdab [0,0,0,0,1,2] ab = ab
    def createTable(self, p):
        table = [0] * len(p)
        i = 1

        # j代表的是公共前缀的长度
        j = 0
        while i < len(p):

            # 说明产生了公共前缀
            if p[i] == p[j]:
                # 公共前缀长度+1
                j += 1
                # 当前遍历到的元素=公共前缀长度
                table[i] = j
                # 去判断下一个元素
                i += 1

            # p[i]，p[j]对不上，没有公共前缀了
            else:
                # 假如说之前有公共前缀的  a b(j) a d(i)
                # 那么i到d的时候，发现b != d
                # 那么表示j要清0，要为下一次的从头到尾扫看有没公共前缀做好准备
                if j > 0:
                    j = table[j - 1]
                # 假如说j原来就没动过
                # 那么我们继续移动i就好了
                else:
                    i += 1
                    j = 0
        return table



    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        table = self.createTable(s + "#" + s[::-1])
        # 输入:abab reverse: baba
        # abab#baba ,前后aba是相同的，table = [0,0,1,2,0,0,1,2,3]
        # 由于abab#baba是绝对回文，但是他有地方可以优化,我们可以把两个公共前缀给优化到只有一个
        # 优化方法就是把s的公共前缀砍掉，然后把他反转拼到s前面
        unsame = s[table[-1]:]
        return unsame[::-1] + s

"""
https://leetcode-cn.com/problems/shortest-palindrome/solution/tu-jie-kmpsuan-fa-by-yangbingjie/
"""