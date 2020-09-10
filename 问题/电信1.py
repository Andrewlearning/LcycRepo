
import sys

def urgyNumber(num):

    res = [1 for i in range(num)]

    p2 = 0
    p3 = 0
    p5 = 0

    for i in range(1, n):
        cur_min = min(res[p2] * 2, res[p3] * 3, res[p5] * 5)
        res[i] = cur_min

        if cur_min == res[p2] * 2:
            p2 += 1
        if cur_min == res[p3] * 3:
            p3 += 1
        if cur_min == res[p5] * 5:
            p5 += 1

    return res[n - 1]




if __name__ == "__main__":

    n = int(sys.stdin.readline().strip())
    print(urgyNumber(n))