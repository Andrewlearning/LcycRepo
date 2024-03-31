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
        self.helper(0)

        return self.res

    def helper(self, startFrom):
        if len(self.temp) > len(self.digits):
            return

        if len(self.temp) == len(self.digits):
            self.res.append("".join(self.temp[:]))
            return

        for i in range(startFrom, len(self.digits)):
            options = self.nm[self.digits[i]]
            for j in options:
                self.temp.append(j)
                self.helper(i + 1)
                self.temp.pop()


"""
与77题相似
"""