class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1 = len(num1) - 1
        p2 = len(num2) - 1

        res = ""
        carry = 0
        while p1 >= 0 or p2 >= 0 or carry:
            cur = carry
            carry = 0
            if p1 >= 0:
                cur += int(num1[p1])
            if p2 >= 0:
                cur += int(num2[p2])

            if cur >= 10:
                cur -= 10
                carry = 1

            # 这里要注意一个顺序的问题
            res = str(cur) + res
            p1 -= 1
            p2 -= 1

        return res