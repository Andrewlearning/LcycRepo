import sys

class Solution():
    def question3(self, level, step):
        self.res = []
        self.helper([], level, step)
        print(len(self.res))

    def helper(self, temp, level, step):
        if sum(temp) == level:
            self.res.append(temp[:])
            return

        if sum(temp) > level:
            return

        for next in range(1, step+1):
            if (len(temp) == 1 and next == temp[-1]) or (len(temp) >= 2 and next in [temp[-1], temp[-2]]):
                continue
            self.helper(temp + [next], level, step)




if __name__ == "__main__":
    data =[]
    while True:
        line = sys.stdin.readline().strip().split()
        if not line:
            break
        data.append(line)

    transfer = list(map(int, data[0]))
    s = Solution()
    s.question3(transfer[0], transfer[1])
