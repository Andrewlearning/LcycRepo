"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 and not word2:
            return 0

        n1 = len(word1)
        n2 = len(word2)

        # dp[i][j] i表示word1[0,i-1]的片段，j表示word2[0,j-1]的片段
        # 合在一起的意思就是word1[0,i-1] 变为 word2[0,j-1]，最少需要多少步操作
        # 之所以长度要设为n+1, 是因为后面有[i-1][j-1]这样的操作，这样做比较方便
        dp = [[0] * (n2+1) for i in range(n1+1)]

        # 边界值，假如说 "" , "abcd" , 那么dp要进行初始化设定, 最极端情况下要更改多少次
        for i in range(n1+1):
            dp[i][0] = i
        for j in range(n2+1):
            dp[0][j] = j

        # 检测出"a",""这种情况，直接返回结果
        if n2 == 0 or n1 == 0:
            return dp[n1][n2]

        # 从1开始是因为[0,1],[1,0]都在上面初始化过了
        # 而且过滤掉n1,n2都为0的情况
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                dp[i][j] = min(dp[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1),
                               dp[i-1][j] + 1,
                               dp[i][j-1] + 1)

        return dp[n1][n2]

"""
https://www.acwing.com/video/1415/
答案：
1.dp[i][j] i表示word1的[0~i]的片段，j表示word2的[0~j]的片段，合在一起的意思就是
word1的[0~i]的片段 和 word2的[0~j]的片段，把他们变成相同的字符串最少需要多少步操作

2.假如说，word1的第i位 和word2的第j位相等，那么就说明早这个位置上不用操作
dp[i][j] = dp[i-1][j-1]

3.当i,j位不相等时，我们有三种操作，delect,insert,replace
这三种操作所针对的都是`word1[i]`字符串

3.1 delect,表示删除第word1[i]位才能保证两个字符串相等，这种情况发生于len(word1[0,i]) > len(word2[0,j]) 
那么前提就是word1[0,i-1] = word2[0,j]可通过dp[i-1][j]次转化达到
所以操作数 dp[i][j] = dp[i-1][j] + 1(这个操作时删掉A)

3.2 insert,表示要在第word1[i]位后面添加一个字母word[j]，才能保证两个字符串相等，这种情况发生于len(word1[0,i]) < len(word2[0,j]) 
那么前提就是word1[0,i] = word2[0,j-1]可通过dp[i][j-1]次转化达到
所以操作数是 dp[i][j] = dp[i][j-1] + 1

3.3 replace, 表示要把第word1[i]，替换成word2[j]，才能保证两字符串相等
但在这个场景下，在word1[i] != word2[j]才要换，
假如word1[i] = word2[j]那么不用换
前提就是word1[0,i-1] = word2[0,j-1]可通过dp[i-1][j-1]
所以操作数是 dp[i][j] = dp[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1)



4.注意我们先得把递归的基础值给设定好，利用两个for循环（假如一个单词是""，另一个单词是x）
5.把两个单词的所有情况都遍历一遍，推出最后的dp[n1][n2]
"""