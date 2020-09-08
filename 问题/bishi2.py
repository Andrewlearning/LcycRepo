
import sys

class Solution():

    def question3(self, pairs):

        if not pairs or len(pairs) == 0:
            return True

        stack = []

        for char in pairs:
            if char in "([{":
                stack.append(char)
            else:
                left = stack.pop(-1)
                if left + char not in "(){}[]":
                    print(left + char)
                    return False
        print(stack)
        return stack == 0



if __name__ == "__main__":
    data =[]
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break
        data.append(line)

    print(data)
    # transfer = list(map(int, data[0]))
    s = Solution()
    print(s.question3(data[0]))

































