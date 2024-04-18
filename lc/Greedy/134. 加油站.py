class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)

        totalTank, curTank = 0, 0
        startFrom = 0
        for i in range(n):
            diff = gas[i] - cost[i]
            totalTank += diff
            curTank += diff

            # 当到达此站，curTank不够油的话，说明不能从上一个出发点出发
            # 同时，由于在到达此站之前都够油，到达此站后就不够油了，说明更不能从此站出发
            # 也说明不够油开往下一站了，所以只能从下一站出发，重新开始统计
            # 假如后面都可以一直开下去的话，说明blocker就在这里，假如sum(gas) >= cost, 说明从后面出发，绕一圈到这里，是够油的
            if curTank < 0:
                # Pick up the next station as the starting one.
                startFrom = i + 1
                # Start with an empty tank.
                curTank = 0

        return startFrom if totalTank >= 0 else -1


"""
算法来说不难， 这题是存在唯一一个点，使得能走完全程
这题有一个规律是，假如说 前面剩的油 + 从上一站到这一站消耗的油-这一站可以补给的油(gas[i] - cost[i]) < 0, 说明已经不够油区下一站了

所以我们假如说要完成任务，我们需要准备两个条件
1. total tank走完全程是正数
2. cur_tank小于0的时候，说明当前节点不行，要换到下一个节0点
"""