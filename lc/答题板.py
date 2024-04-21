

def solve():
    n = nc = 6

    for val in range(1, 37):

        row = (val - 1) // nc
        col = (val - 1) % nc

        if row % 2 == 1:
            col = n - 1 - col
        row = n - 1 - row

        print(val, (row,col))

if __name__ == '__main__':
    print(solve())