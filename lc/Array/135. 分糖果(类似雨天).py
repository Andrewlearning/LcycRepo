class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0

        # 我们先初始化，先假设每个位置上的孩子都是评价最低的
        candy = [1] * len(ratings)

        for i in range(1, len(ratings)):
            # 假如candy[i] > candy[i-1]了，那么需要给i小朋友发糖, 让i小朋友的糖比i-1小朋友多1
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1


        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                # 假如candy[i] > candy[i+1]了，那么我们就不用给i小朋友发糖了
                # 假如candy[i] == candy[i+1], 那么需要给i小朋友发糖，比i+1多一颗
                candy[i] = max(candy[i], candy[i + 1] + 1)

        return sum(candy)

"""
 // Time: O(n), Space: O(n)
https://algocasts.io/episodes/dbGYvyp5
这个答案不能通用，但是比较好记忆
"""