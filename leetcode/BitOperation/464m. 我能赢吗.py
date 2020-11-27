"""
在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和达到或超过 100 的玩家，即为胜者。
如果我们将游戏规则改为 “玩家不能重复使用整数” 呢？
例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。
给定一个整数 maxChoosableInteger （整数池中可选择的最大数）和另一个整数 desiredTotal（累计和），判断先出手的玩家是否能稳赢（假设两位玩家游戏时都表现最佳）？
你可以假设 maxChoosableInteger 不会大于 20， desiredTotal 不会大于 300。

示例：

输入：
maxChoosableInteger = 10
desiredTotal = 11

输出：
false

解释：
无论第一个玩家选择哪个整数，他都会失败。
第一个玩家可以选择从 1 到 10 的整数。
如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。
"""
class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        
        # 每一个数字代表一种状态，每一位上的1代表已经被选过的数，0代表尚未选择的数
        self.f = [None] * (1 << maxChoosableInteger)
        self.n = maxChoosableInteger
        self.m = desiredTotal

        # 假如说所有数字的和加起来都没有 终点多，说明是错的
        if (self.n * (self.n + 1) // 2 < self.m):
            return False

        return self.helper(0)
    

    def helper(self, x):
        # 假如说当前状态已经被更改过了，可以直接返回结果
        if self.f[x] != None:
            return self.f[x]
        
        total = 0

        for i in range(0, self.n):
            # bit:     5 4 3 2 1 0
            # 代表的数:  6 5 4 3 2 1
            if x >> i & 1:
                total += i + 1
        
        
        for i in range(self.n):
            # 假如当前位上是1，说明之前这个数字已经被别人选过了，跳过
            if x >> i & 1:
                continue
            # 假如当前状态 + 选择了第i个数字，大于终点，说明这个状态是可以赢的
            if total + i + 1 >= self.m:
                self.f[x] = True
                return self.f[x]
            # 遍历所有对手可能从哪个状态开始选数字
            # 假如说存在一个状态，使得对手怎么选的都是输，那我们必胜，
            if self.helper(x + (1 << i)) == False:
                self.f[x] = True
                return self.f[x]
        
        # 假如上面所有取胜条件我们都满足不了
        # 说明在当前状态开始选数字必败
        self.f[x] = False
        return self.f[x]

# https://www.acwing.com/video/1866/



