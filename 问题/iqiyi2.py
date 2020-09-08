import sys

class Solution():
    def question2(self, dirs):

        memo = []
        i, j = 0, 0

        for char in dirs:
            if char == "N":
                i += 1
                if (i,j) in memo:
                    return True
                memo.append((i,j))
            elif char == "S":
                i -= 1
                if (i,j) in memo:
                    return True
                memo.append((i,j))
            elif char == "W":
                j -= 1
                if (i,j) in memo:
                    return True
                memo.append((i,j))
            elif char == "E":
                j += 1
                if (i,j) in memo:
                    return True
                memo.append((i,j))

        return False



if __name__ == "__main__":
    data =[]
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        data.append(line)


    s = Solution()
    print(s.question2(data[0]))

































