
import sys

class Solution():
    def question1(self, num):
        res = []
        for a in range(0, 10):
            for b in range(0, 10):
                for c in range(0, 10):
                    num1 = a * 100 + b * 10 + c * 1
                    num2 = a * 100 + c * 10 + c * 1
                    if num1 + num2 == num:
                        res.append([num1, num2])
        print(len(res))
        for pair in res:
            temp = " ".join(list(map(str, pair)))
            print(temp)


if __name__ == "__main__":
    data =[]
    while True:
        line = sys.stdin.readline().strip().split()
        if not line:
            break
        data.append(line)

    transfer = list(map(int, data[0]))
    # print(transfer)
    s = Solution()
    s.question1(transfer[0])


































