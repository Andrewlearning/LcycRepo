import sys

class Solution():
    def question1(self, n):
        res = 0
        while n != 0:
            res += n // 5
            n //= 5
        return res




if __name__ == "__main__":
    data =[]
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        data.append(line)

    print(data)
    s = Solution()
    print(s.question1(int(data[0])))

































