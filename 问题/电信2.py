import sys


def q2():
    res = []
    for a in range(1, 10):
        for b in range(a+1, 10):
            for c in range(b+1, 10):
                for d in range(c+1, 10):
                    if a * 1000 + b * 100 + c * 10 + d + b * 1000 + c * 100 + d * 10 + a == 8888:
                        res.append(str(a) + " " + str(b) + " " + str(c) + " " + str(d))

    for item in res:
        print(item)


if __name__ == "__main__":
    q2()