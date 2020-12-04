"""
给你一个数组 prices ，其中 prices[i] 是商店里第 i 件商品的价格。

商店里正在进行促销活动，如果你要买第 i 件商品，那么你可以得到与 prices[j] 相等的折扣，其中 j 是满足 j > i 且 prices[j] <= prices[i] 的 最小下标 ，如果没有满足条件的 j ，你将没有任何折扣。

请你返回一个数组，数组中第 i 个元素是折扣后你购买商品 i 最终需要支付的价格。
示例 1：

输入：prices = [8,4,6,2,3]
输出：[4,2,4,2,3]
解释：
商品 0 的价格为 price[0]=8 ，你将得到 prices[1]=4 的折扣，所以最终价格为 8 - 4 = 4 。
商品 1 的价格为 price[1]=4 ，你将得到 prices[3]=2 的折扣，所以最终价格为 4 - 2 = 2 。
商品 2 的价格为 price[2]=6 ，你将得到 prices[3]=2 的折扣，所以最终价格为 6 - 2 = 4 。
商品 3 和 4 都没有折扣。
示例 2：

输入：prices = [1,2,3,4,5]
输出：[1,2,3,4,5]
解释：在这个例子中，所有商品都没有折扣。
"""

class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """

        # 储存还没碰到比自己小的价格下标
        # 因为碰到比自己小的就会被pop出，所以都在一个单调栈里的话说明里面的价格是从小到大
        stack = []

        for i in range(len(prices)):
            # 当栈有元素 且 栈里最大的元素比当前价格高，说明可以操作
            while len(stack) and prices[stack[-1]] >= prices[i]:
                # 更新 高价-低价
                prices[stack[-1]] -= prices[i]
                # 因为我们只能-最近低价，只能操作一次，所以减完这个高价就要pop掉
                stack.pop()

            # 每次都把当前元素加进stack,因为我们不知道后面需不需对它进行减价处理
            stack.append(i)

        return prices

# https://www.youtube.com/watch?v=X98Yc4YtgyA&list=PLLuMmzMTgVK6AGnp5TEVoqglnIKn1Njxp&index=2