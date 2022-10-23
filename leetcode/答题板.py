

def solve(m, strings):
    # map = []
    # for i in range(26):
    #     map.append(chr(97 + i))
    # print(map)
    # print(ord("a"))

    res = 0
    for s in strings:
        temp = 1
        for char in s:
            # print("ord", int(ord(char)))
            temp *= ord(char)

        print(temp)
        res += temp
    if res % 2 == 0:
        return "EVEN"
    return "ODD"

if __name__ == '__main__':
    print(solve(2, ["azbde", "abcher", "acegk"]))