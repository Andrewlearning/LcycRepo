# def kth_difference(k, array):
#     diff_pair = []
#     for i in range(len(array)):
#         for j in range(i + 1, len(array)):
#             if i != j:
#                 diff_pair.append(abs(array[i] - array[j]))
#
#     diff_pair.sort()
#     return diff_pair[k - 1]
#
# print(kth_difference(1, [23, 80, 88, 91, 23]))
# print(kth_difference(2, [23, 80, 88, 91, 23]))
# print(kth_difference(3, [23, 80, 88, 91, 23]))
# print(kth_difference(3, [1, 2, 3, 4]))

array = [[0,1,0,1,0],
         [1,0,1,0,0],
         [0,1,0,0,0],
         [0,0,0,1,0]]

def ladder_n(table, n):
    res = set()
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == 1:
                count = 1
                p_i = i
                p_j = j
                while 0 <= p_i - 1 <= len(table) and \
                    0 <= p_j + 1 <= len(table[i]) and table[p_i][p_j] == 1:
                    count += 1
                    p_i -= 1
                    p_j += 1
                res.add(count)

    return n in res

array = [[0,1,0,1,0],
         [1,0,1,0,0],
         [0,1,0,0,0],
         [0,0,0,1,0]]

print(ladder_n(array, 1))
print(ladder_n(array, 2))
print(ladder_n(array, 3))
print(ladder_n(array, 4))







