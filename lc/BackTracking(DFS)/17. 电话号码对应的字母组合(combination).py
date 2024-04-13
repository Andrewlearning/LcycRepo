class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []

        self.nm = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        self.res = []
        self.temp = []
        self.digits = digits
        self.n
        self.helper(0)

        return self.res

    def helper(self, startFrom):
        if len(self.temp) > self.n:
            return

        if len(self.temp) == self.n:
            self.res.append("".join(self.temp[:]))
            return

        for i in range(startFrom, self.n):
            options = self.nm[self.digits[i]]
            for j in options:
                self.temp.append(j)
                self.helper(i + 1)
                self.temp.pop()


"""
与77题相似
"""