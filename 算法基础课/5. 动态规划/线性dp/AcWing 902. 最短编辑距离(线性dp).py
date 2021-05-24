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
        if not word1 and not word2: return 0

        m = len(word1)
        n = len(word2)

        # dp[i][j] i表示word1的1-i的片段，j表示word2的1-j的片段，合在一起的意思就是
        # word1的1-i的片段 和 word2的1-j的片段，把他们变成相同的字符串最少需要多少步操作
        dp = [[0] * (n+1) for i in range(m+1)]

        # 边界值，假如说 "" , "abcd" , 那么dp要进行初始化设定, 最极端情况下要更改多少次
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j

        # 检测出"a",""这种情况，直接返回结果
        if n == 0 or m == 0:
            return dp[m][n]

        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j] = min(dp[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1),
                               dp[i-1][j] + 1,
                               dp[i][j-1] + 1)

        return dp[m][n]

"""
lc72
https://www.acwing.com/video/334/
答案：
1.dp[i][j] i表示word1的1-i的片段，j表示word2的1-j的片段，合在一起的意思就是
word1的1-i的片段 和 word2的1-j的片段，把他们变成相同的字符串最少需要多少步操作

2.假如说，word1的第i位 和word2的第j位相等，那么就说明在这个index上不用操作
dp[i][j] = dp[i-1][j-1]

3.当i,j位不相等时，我们有三种操作，delect,insert,replace, 这三种操作所针对的都是i字符串
3.1 delect,表示删除第i位能保证两个字符串相等，
那么前提就是[1,i-1] == [1,j], 所以进行的操作数是[i-1][j] + 1

3.2 insert,表示要在第i位后面添加一个字母，才能保证两个字符串相等
那么前提就是[1,i] == [1,j-1], 因为要让[i+1] == [j]嘛，所以操作数是[i][j-1] + 1

3.3 replace,表示要把第i位字母，替换成别的字母，才能保证两字符串相等
那么现在就说明[i] != [j]所以才要换，那更换成功的基础是，[1,i-1] == [1,j-1]，
要不然换了也没用，所以这里的操作 [i-1][j-1] + 0/1, 有可能为0的情况是[i] 有可能等于 [j]

  
4.注意我们先得把递归的基础值给设定好，利用两个for循环（假如一个单词是""，另一个单词是x）
5.把两个单词的所有情况都遍历一遍，推出最后的dp[m][n]

remark:
注意最后两个for循环是从1开始的，因为中途判断word1[i-1] == word2[j-1],不从1开始会
有index错误， 同时我们直到dp[0][0] = 0 ,[0][1],[1][0]都是有预设值的，所以可以不必
遍历他们


"""