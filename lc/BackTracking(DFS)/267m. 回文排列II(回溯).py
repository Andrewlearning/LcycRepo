import collections
class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.hashmap = collections.Counter(s)
        # 出现奇数次的元素
        self.odd = 0
        self.res = []
        for count in self.hashmap.values():
            if count % 2 == 1:
                self.odd += 1

        # 假如说字符串里出现奇数次的元素大于1，说明就不能用于构成回文串了
        if self.odd > 1:
            return []

        temp = ""
        # 假如说存在奇数次元素，那么把它放在中间
        for key in self.hashmap:
            if self.hashmap[key] % 2 == 1:
                temp += key
                self.hashmap[key] -= 1

        # 进行回溯
        self.helper(temp, len(s))
        return self.res

    def helper(self, temp, n):
        if len(temp) > n:
            return

        if len(temp) == n:
            self.res.append(temp[:])

        # 在这里我们构造回文串，进行回溯
        for key in self.hashmap:
            if self.hashmap[key] > 1:
                self.hashmap[key] -= 2
                self.helper(key + temp + key, n)
                self.hashmap[key] += 2

        return


"""
https://www.youtube.com/watch?v=GOB9i4HOu9U
"""