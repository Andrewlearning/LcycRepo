class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return False

        s = 0
        # 因为 1 * 自己，这种情况开始考虑
        # 所以我们要从1开始遍历
        # 然后另外为什么是 sqrt(num) + 1, 是因为我们要考虑到6*6=36这种情况
        # 所以要给sqrt(36) + 1, 留空间
        # 然后假如说i再大的话，就会出现重复的情况，例如 3 * 4 和 4 * 3
        for i in range(1, int(sqrt(num)) + 1):
            if num % i == 0:
                s += (i + num // i)

        # 因为 在因数为[1,num]的时候，把自己的值也加进去了一次
        if s == 2 * num:
            return True
        return False
