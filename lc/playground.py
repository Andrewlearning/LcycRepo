list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped = zip(list1, list2)  # 将两个列表进行zip
print(zipped)
print(list(zipped))

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [10, 20, 30]

for a, b, c in zip(list1, list2, list3):
    print(a, b, c)